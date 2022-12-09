from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

### By default every return value is pushed to xcoms
### xcoms can only be called by task instance
### max size of xcoms is 48kb
default_args = {
    "owner": "shubhushan",
    "retries": 4,
    "retry_delay": timedelta(minutes=1)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids="get_name", key='first_name')
    last_name = ti.xcom_pull(task_ids="get_name", key='last_name')
    print(f"Weelcome {first_name} {last_name}")

def get_name(ti):
    ti.xcom_push(key="first_name", value="shubhushan")
    ti.xcom_push(key="last_name", value="kattel")

with DAG(default_args=default_args,
        dag_id='xcom_tutorial',
        start_date=datetime(2022,12,9, 9),
        schedule_interval= "*/20 * * * *"
        ) as dag:
    task1 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task2 = PythonOperator(
        task_id="print_name",
        python_callable=greet
    )

    task1 >> task2