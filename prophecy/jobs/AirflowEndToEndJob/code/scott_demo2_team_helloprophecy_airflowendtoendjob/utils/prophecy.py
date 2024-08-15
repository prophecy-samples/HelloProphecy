from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/gold_sales": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_sales-1.0-py3-none-any.whl", 
    "pipelines/gold_top_customers": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_top_customers-1.0-py3-none-any.whl", 
    "pipelines/raw_bronze": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/raw_bronze-1.0-py3-none-any.whl", 
    "pipelines/silver_customers_orders": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/silver_customers_orders-1.0-py3-none-any.whl", 
    "pipelines/silver_zip_codes": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/silver_zip_codes-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/silver_customers_orders": "silver_customers_orders", 
    "pipelines/silver_zip_codes": "silver_zip_codes", 
    "pipelines/gold_sales": "gold_sales", 
    "pipelines/gold_top_customers": "gold_top_customers", 
    "pipelines/raw_bronze": "raw_bronze"
}
