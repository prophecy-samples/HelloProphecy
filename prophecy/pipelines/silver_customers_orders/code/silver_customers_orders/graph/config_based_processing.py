from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver_customers_orders.config.ConfigStore import *
from silver_customers_orders.udfs.UDFs import *

def config_based_processing(spark: SparkSession, in0: DataFrame) -> DataFrame:
    Config = json.load("config.json")[Config.ENVIRONMENT]

    return out0
