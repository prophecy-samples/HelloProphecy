from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from gold_top_customers.config.ConfigStore import *
from gold_top_customers.udfs.UDFs import *
from prophecy.utils import *
from gold_top_customers.graph import *

def pipeline(spark: SparkSession) -> None:
    df_silver_customers = silver_customers(spark)
    df_gold_total_sales_by_customer = gold_total_sales_by_customer(spark)
    df_OrderByTotalSpend = OrderByTotalSpend(spark, df_gold_total_sales_by_customer)
    df_Top50 = Top50(spark, df_OrderByTotalSpend)
    df_silver_irs_zipcode = silver_irs_zipcode(spark)
    df_JoinCustomerInfo = JoinCustomerInfo(spark, df_Top50, df_silver_customers, df_silver_irs_zipcode)
    gold_top50_customers_by_spend(spark, df_JoinCustomerInfo)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/gold_top_customers")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/gold_top_customers")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
