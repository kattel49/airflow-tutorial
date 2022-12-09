from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    "owner": "shubhushan",
    "retries": 4,
    'retry_delay': timedelta(minutes=1)
}

@dag(dag_id='dag_with_taskflow',
    default_args=default_args,
    start_date=datetime(2022, 12, 9, 10),
    schedule_interval= '*/20 * * * *'
    )
def hello_world_etl():
    
    @task()
    def get_name():
        return "Shubhushan"
    
    @task()
    def get_age():
        return 22
    
    @task
    def greet(name, age):
        print(f"Hello, my name is {name}. I am {age} years old!")
    
    name = get_name()
    age = get_age()
    greet(name=name, age=age)

greet_dag = hello_world_etl()