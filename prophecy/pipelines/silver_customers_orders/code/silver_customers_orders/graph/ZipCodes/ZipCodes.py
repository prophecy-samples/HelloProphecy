from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def ZipCodes(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_silver_irs_zipcode = silver_irs_zipcode(spark)
    df_UniqueZipCodes = UniqueZipCodes(spark, df_silver_irs_zipcode)

    return df_UniqueZipCodes
