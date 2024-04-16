from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gold_top_customers.config.ConfigStore import *
from gold_top_customers.udfs.UDFs import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/gold_top_customers")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/gold_top_customers", config = Config)(pipeline)

if __name__ == "__main__":
    main()
