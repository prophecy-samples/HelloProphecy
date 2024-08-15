package io.prophecy.pipelines.gold_top_customers.graph

import io.prophecy.libs._
import io.prophecy.pipelines.gold_top_customers.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object gold_top50_customers_by_spend {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("delta")
      .mode("overwrite")
      .saveAsTable("`scottdemoscala`.`gold_top50_customers_by_spend`")

}
