from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta
from airflow.models import Variable

from extract import extract_data
from transform import transform_data


with DAG(
  'etl_twitter_pipeline',
  description="A simple twitter ETL pipeline using Python,PostgreSQL and Apache Airflow",
  start_date=datetime(year=2023, month=2, day=5),
  schedule_interval=timedelta(minutes=5)
) as dag:
  
  start_pipeline = DummyOperator(
		task_id='start_pipeline',
	)
  
  create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres_connection',
    sql='sql/create_table.sql'
  )
  
  extract_data = PythonOperator(
    task_id = 'extract_data',
    python_callable = extract_data,
  )

  csv_path = Variable.get('csv_file')

  transform_data = PythonOperator(
      task_id = 'transform_data',
      python_callable = transform_data,
      op_kwargs={'data': csv_path}
  )
    
  load_data = PostgresOperator(
      task_id='load_data_into_postgresql',
      postgres_conn_id='postgres_connection',
      sql=["""TRUNCATE TABLE twitter_etl_table""",
          """COPY twitter_etl_table FROM %(csv)s
          DELIMITER ',' CSV HEADER;"""
          ],
      parameters={'csv': csv_path}
  )
    
  end_pipeline = DummyOperator(
      task_id='end_pipeline',
  )


start_pipeline >> create_table >> extract_data >> transform_data >> load_data >> end_pipeline