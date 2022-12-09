#!/bin/bash
curl -LfO https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GIT=0" > .env