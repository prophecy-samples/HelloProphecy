from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *

def gold_sales_by_zip_date(spark: SparkSession, in0: DataFrame):
    if spark.catalog._jcatalog.tableExists(f"scottdemo.gold_sales_by_zip_date"):
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, f"scottdemo.gold_sales_by_zip_date")\
            .alias("target")\
            .merge(
              in0.alias("source"),
              (
                (col("source.zipcode") == col("target.zipcode"))
                & (col("source.order_date") == col("target.order_date"))
              )
            )\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").saveAsTable(f"scottdemo.gold_sales_by_zip_date")
