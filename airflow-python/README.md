## Installation via python
```sh
virtualenv venv
source venv/bin/activate
pip install 'apache-airflow==2.5.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW_HOME=$(pwd)
airflow db init
airflow users create --username admin --firstname firstname \
    --lastname lastname --role Admin
    --email x@gmail.com --password password
```
Input your local python version in constraints-{python-version}.txt<br>
Create a user for airflow<br>