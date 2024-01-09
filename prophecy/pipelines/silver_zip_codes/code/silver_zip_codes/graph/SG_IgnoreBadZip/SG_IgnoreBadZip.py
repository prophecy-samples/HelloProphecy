from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def SG_IgnoreBadZip(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_IgnoreBadZip_1 = IgnoreBadZip_1(spark, in0)
    subgraph_config.update(Config)

    return df_IgnoreBadZip_1
