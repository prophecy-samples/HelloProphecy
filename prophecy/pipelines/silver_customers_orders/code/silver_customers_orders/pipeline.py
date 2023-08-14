from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs.UDFs import *
from prophecy.utils import *
from silver_customers_orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_bronze_orders = bronze_orders(spark)
    silver_orders(spark, df_bronze_orders)
    df_bronze_customers = bronze_customers(spark)
    df_silver_irs_zipcode = silver_irs_zipcode(spark)
    df_UniqueZipCodes = UniqueZipCodes(spark, df_silver_irs_zipcode)
    df_CustomerZipCodes = CustomerZipCodes(spark, df_bronze_customers, df_UniqueZipCodes)
    silver_customers(spark, df_CustomerZipCodes)
    df_ByCustomerId = ByCustomerId(spark, df_bronze_orders, df_CustomerZipCodes)
    silver_order_customer_details(spark, df_ByCustomerId)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/silver_customers_orders")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/silver_customers_orders", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/silver_customers_orders")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
