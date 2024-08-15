from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/gold_sales": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_sales.jar", 
    "pipelines/gold_top_customers": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/gold_top_customers.jar", 
    "pipelines/raw_bronze": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/raw_bronze.jar", 
    "pipelines/silver_customers_orders": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/silver_customers_orders.jar", 
    "pipelines/silver_zip_codes": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/silver_zip_codes.jar"
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
    "pipelines/silver_customers_orders": "io.prophecy.pipelines.silver_customers_orders.Main", 
    "pipelines/silver_zip_codes": "io.prophecy.pipelines.silver_zip_codes.Main", 
    "pipelines/gold_sales": "io.prophecy.pipelines.gold_sales.Main", 
    "pipelines/gold_top_customers": "io.prophecy.pipelines.gold_top_customers.Main", 
    "pipelines/raw_bronze": "io.prophecy.pipelines.raw_bronze.Main"
}
