from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from gold_sales.config.ConfigStore import *
from gold_sales.udfs.UDFs import *

def gold_total_sales_by_customer(spark: SparkSession, in0: DataFrame):
    if spark.catalog._jcatalog.tableExists(f"scottdemo.gold_total_sales_by_customer"):
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, f"scottdemo.gold_total_sales_by_customer")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.customer_id") == col("target.customer_id")))\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").saveAsTable(f"scottdemo.gold_total_sales_by_customer")
