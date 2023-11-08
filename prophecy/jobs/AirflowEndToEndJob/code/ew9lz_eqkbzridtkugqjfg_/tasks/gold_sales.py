def gold_sales():
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "gold_sales",
        json = {
          "task_key": "gold_sales", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "12.2.x-scala2.12", 
            "num_workers": 1, 
            "custom_tags": {}, 
            "spark_conf": {
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/AirflowEndToEndJob", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "6726", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.prophecy.packages.path": "{\"pipelines/silver_customers_orders\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/silver_customers_orders-1.0-py3-none-any.whl\",\"pipelines/silver_zip_codes\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/silver_zip_codes-1.0-py3-none-any.whl\",\"pipelines/gold_sales\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_sales-1.0-py3-none-any.whl\",\"pipelines/gold_top_customers\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_top_customers-1.0-py3-none-any.whl\",\"pipelines/raw_bronze\":\"dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/raw_bronze-1.0-py3-none-any.whl\"}", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": False, 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.app.prophecy.io/eventws"
            }, 
            "driver_node_type_id": "i3.xlarge", 
            "aws_attributes": {}
          }, 
          "python_wheel_task": {
            "package_name": "gold_sales", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.25"}},                          {"pypi" : {"package" : "prophecy-libs==1.6.9"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_sales-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "mOktW1DX4uyaf3C4r2GRI",
    )
