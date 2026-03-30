from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.extract import run_extract
from src.clean import run_clean
from src.clean_append_to_database import run_load

default_args = {
    "owner": "michal",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="crypto_data_pipeline",
    default_args=default_args,
    description="Daily crypto data extraction pipeline",
    start_date=datetime(2026, 3, 30),
    schedule="0 10 * * *",  # Daily at 10:00 AM
    catchup=True, # Want to make sure it'll catchup when I turn on my computer
    tags=["crypto", "portfolio"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_crypto_data",
        python_callable=run_extract,
    )

    clean_task = PythonOperator(
        task_id="clean_crypto_data",
        python_callable=run_clean,
    )

    load_task = PythonOperator(
        task_id="load_crypto_data",
        python_callable=run_load,
    )

    extract_task >> clean_task >> load_task