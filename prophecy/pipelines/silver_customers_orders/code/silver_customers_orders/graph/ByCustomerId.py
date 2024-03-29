from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs.UDFs import *

def ByCustomerId(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.customer_id") == col("in1.customer_id")), "inner")\
        .select(col("in0.order_id").alias("order_id"), col("in0.order_date").alias("order_date"), col("in0.amount").alias("amount"), col("in0.customer_id").alias("customer_id"), col("in1.account_open_date").alias("account_open_date"), col("in1.first_name").alias("first_name"), col("in1.last_name").alias("last_name"), col("in1.zipcode").alias("zipcode"), col("in1.account_flags").alias("account_flags"))
