# twitter_etl_airflow

## A Twitter ETL pipeline using Python, PostgreSQL and Apache Airflow
**![Blog Link](https://www.freecodecamp.org/news/orchestrate-an-etl-data-pipeline-with-apache-airflow/)**

<br />

![etl pipeline](/img/airflow_etl.jpg)

<br />


# The Pipeline Architecture:

## 1) Data is obtained from Twitter.
## 2) Data cleaning is performed using Python.
## 3) The cleansed dataset is imported into a PostgreSQL database through the use of Apache Airflow hooks and Operators.

<br />

## Apache Airflow takes care of monitoring and scheduling this pipeline
