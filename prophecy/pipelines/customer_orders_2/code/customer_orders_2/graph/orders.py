from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from customer_orders_2.config.ConfigStore import *
from customer_orders_2.udfs.UDFs import *

def orders(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", IntegerType(), True), StructField("customer_id", IntegerType(), True), StructField("order_status", StringType(), True), StructField("order_category", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", DoubleType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .option("ignoreLeadingWhiteSpace", True)\
        .option("ignoreTrailingWhiteSpace", True)\
        .csv("dbfs:/Prophecy/scott+demo2@prophecy.io/OrdersDatasetInput.csv")
