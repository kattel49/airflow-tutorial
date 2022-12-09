from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    "owner":"shubhushan",
    "retries" : 5,
    "retry_delay": timedelta(minutes=1)
}

def greet(name):
    print(f"Hello World! {name}")

with DAG(dag_id="first_python_dag",
            default_args=default_args,
            description="Testing python operator",
            start_date=datetime(2022, 12, 9, 9),
            schedule_interval="*/10 * * * *"
) as dag:
    task1 = PythonOperator(
        task_id="greet_users",
        python_callable=greet,
        op_kwargs={"name": "Shubhushan"}
    )
    task1