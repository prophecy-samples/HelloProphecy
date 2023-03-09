from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def CleanupSubgraph(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_Cleanup = Cleanup(spark, in0)

    return df_Cleanup
