import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from ew9lz_eqkbzridtkugqjfg_.tasks import gold_sales, gold_top_customers, raw_bronze, silver_customers, silver_zip_codes
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "eW9lz_eqKBZRiDTKugqJfg_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "FAsMEzD_"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2023, 11, 29, tz = "UTC"), 
    catchup = True
) as dag:
    silver_customers_op = silver_customers()
    raw_bronze_op = raw_bronze()
    gold_top_customers_op = gold_top_customers()
    silver_zip_codes_op = silver_zip_codes()
    gold_sales_op = gold_sales()
    raw_bronze_op >> silver_zip_codes_op
    silver_zip_codes_op >> silver_customers_op
    silver_customers_op >> gold_sales_op
    gold_sales_op >> gold_top_customers_op
