from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_top_customers.config.ConfigStore import *
from gold_top_customers.udfs.UDFs import *

def JoinCustomerInfo(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.customer_id") == col("in1.customer_id")), "inner")\
        .join(in2.alias("in2"), (col("in1.zipcode") == col("in2.zipcode")), "inner")\
        .select(col("in0.orders").alias("orders"), col("in0.total_spend").alias("total_spend"), col("in0.customer_id").alias("customer_id"), col("in1.first_name").alias("first_name"), col("in1.last_name").alias("last_name"), col("in1.phone").alias("phone"), col("in1.email").alias("email"), col("in1.zipcode").alias("zipcode"), col("in2.state").alias("state"), col("in2.is_high_income").alias("zipcode_is_high_income"), col("in1.account_open_date").alias("account_open_date"), col("in1.account_flags").alias("account_flags"))
