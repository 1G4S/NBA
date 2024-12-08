import datetime
import os
from dotenv import load_dotenv

from airflow import DAG
from airflow.operators.python import PythonOperator

from extract.extract import Extract
from transform.transform import Transform

from load.load import Load

from extract.strategies.stadiums_retrieval_strategy import StadiumsRetrievalStrategy
from transform.strategies.stadiums_transform_strategy import StadiumsTransformStrategy
from load.strategies.stadiums_load_strategy import StadiumsLoadStrategy

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT_MAIN = os.getenv('ENDPOINT_MAIN')
ENDPOINT_STADIUMS = os.getenv('ENDPOINT_STADIUMS')
DB_CONNECTION = os.getenv('DB_CONNECTION')


def extract_stadiums(**kwargs):
    print('Current dir: ', os.getcwd())
    stadiums_extract_strategy = StadiumsRetrievalStrategy(
        api_key=API_KEY,
        endpoint_main=ENDPOINT_MAIN,
        endpoint_stadiums=ENDPOINT_STADIUMS
    )
    stadiums_extract = Extract(stadiums_extract_strategy)
    kwargs['ti'].xcom_push(
        key='stadiums_raw_data',
        value=stadiums_extract.save_data()
    )


def transform_stadiums(**kwargs):
    file_path = kwargs['ti'].xcom_pull(
        task_ids='extract_stadiums',
        key='stadiums_raw_data'
    )
    stadiums_transform_strategy = StadiumsTransformStrategy(
        path_to_data=file_path
    )
    stadiums_transform = Transform(stadiums_transform_strategy)
    kwargs['ti'].xcom_push(key='stadiums_prepared_data',
                           value=stadiums_transform.get_clean_data())


def load_stadiums(**kwargs):
    stadiums_prepared_data = kwargs['ti'].xcom_pull(
        task_ids='transform_stadiums',
        key='stadiums_prepared_data'
    )
    stadiums_load_strategy = StadiumsLoadStrategy(stadiums_prepared_data, DB_CONNECTION)
    stadiums_load = Load(stadiums_load_strategy)
    stadiums_load.load_prepared_data()


default_args = {
    'owner': 'admin',
    'start_date': datetime.datetime(2024, 12, 7),
    'retries': 0
}

with DAG(
        dag_id='stadiums_dag',
        default_args=default_args,
        schedule_interval='@daily'
) as dag:
    extract = PythonOperator(
        task_id='extract_stadiums',
        python_callable=extract_stadiums
    )

    transform = PythonOperator(
        task_id='transform_stadiums',
        python_callable=transform_stadiums
    )

    load = PythonOperator(
        task_id='load_stadiums',
        python_callable=load_stadiums
    )

extract >> transform >> load
