## Running airflow with docker
```
./download-airflow.sh
docker compose up airflow-init
```
Remove all features that pertain to celery, delete the celery worker, and flower from the yaml file.<br>
