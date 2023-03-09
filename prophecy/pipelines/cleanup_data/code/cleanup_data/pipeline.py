from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup_data.config.ConfigStore import *
from cleanup_data.udfs.UDFs import *
from prophecy.utils import *
from cleanup_data.graph import *

def pipeline(spark: SparkSession) -> None:
    df_CleanupSubgraph = CleanupSubgraph(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/cleanup_data")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/cleanup_data")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
