from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta


with DAG(
  'etl_twitter_pipeline',
  description="A simple twitter ETL pipeline using Python,PostgreSQL and Apache Airflow",
  start_date=datetime(year=2023, month=2, day=5),
  schedule_interval=timedelta(minutes=5)
) as dag:
  
  start_pipeline = DummyOperator(
		task_id='start_pipeline',
	)
  
 

start_pipeline 