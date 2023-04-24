from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customer_orders_2.config.ConfigStore import *
from customer_orders_2.udfs.UDFs import *
from prophecy.utils import *
from customer_orders_2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_customers = customers(spark)
    df_By_CustomerId = By_CustomerId(spark, df_orders, df_customers)
    df_Cleanup = Cleanup(spark, df_By_CustomerId)
    df_Sum_Amounts = Sum_Amounts(spark, df_Cleanup)
    Customer_Orders(spark, df_Sum_Amounts)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customer_orders_2")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/customer_orders_2")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
