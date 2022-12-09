from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'shubhushan',
    'retries': 4,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id="First_DAG",
    default_args=default_args,
    description="First DAG ever made",
    start_date=datetime(2022, 12, 9, 9),
    schedule_interval='*/10 * * * *'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo this is the first task"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hey, I will run after task 2"
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo Hey, I will run along with task 2 after task 1"
    )
    # method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # method 2
    #task1 >> task2
    #task1 >> task3

    # method 3
    task1 >> [task2, task3]