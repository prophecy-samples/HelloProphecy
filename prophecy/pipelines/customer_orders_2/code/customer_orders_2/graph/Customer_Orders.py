from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from customer_orders_2.config.ConfigStore import *
from customer_orders_2.udfs.UDFs import *

def Customer_Orders(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .option("ignoreLeadingWhiteSpace", True)\
        .option("ignoreTrailingWhiteSpace", True)\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/Prophecy/scott+demo2@prophecy.io/CustomersOrders.csv")
