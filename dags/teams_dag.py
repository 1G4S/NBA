import datetime
import os
from dotenv import load_dotenv

from airflow import DAG
from airflow.operators.python import PythonOperator

from extract.extract import Extract
from transform.transform import Transform

from load.load import Load

from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy
from transform.strategies.teams_transform_strategy import TeamsTransformStrategy
from load.strategies.teams_load_strategy import TeamsLoadStrategy

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT_MAIN = os.getenv('ENDPOINT_MAIN')
ENDPOINT_TEAMS = os.getenv('ENDPOINT_TEAMS')
DB_CONNECTION = os.getenv('DB_CONNECTION')


def extract_teams(**kwargs):
    print('Current dir: ', os.getcwd())
    teams_extract_strategy = TeamsRetrievalStrategy(
        api_key=API_KEY,
        endpoint_main=ENDPOINT_MAIN,
        endpoint_teams=ENDPOINT_TEAMS
    )
    teams_extract = Extract(teams_extract_strategy)
    kwargs['ti'].xcom_push(
        key='teams_raw_data',
        value=teams_extract.save_data()
    )


def transform_teams(**kwargs):
    file_path = kwargs['ti'].xcom_pull(
        task_ids='extract_teams',
        key='teams_raw_data'
    )
    teams_transform_strategy = TeamsTransformStrategy(
        path_to_data=file_path
    )
    teams_transform = Transform(teams_transform_strategy)
    kwargs['ti'].xcom_push(key='teams_prepared_data',
                           value=teams_transform.get_clean_data())


def load_teams(**kwargs):
    teams_prepared_data = kwargs['ti'].xcom_pull(
        task_ids='transform_teams',
        key='teams_prepared_data'
    )
    teams_load_strategy = TeamsLoadStrategy(teams_prepared_data, DB_CONNECTION)
    teams_load = Load(teams_load_strategy)
    teams_load.load_prepared_data()


default_args = {
    'owner': 'admin',
    'start_date': datetime.datetime(2024, 12, 7),
    'retries': 0
}

with DAG(
        dag_id='teams_dag',
        default_args=default_args,
        schedule_interval='@daily'
) as dag:
    extract = PythonOperator(
        task_id='extract_teams',
        python_callable=extract_teams
    )

    transform = PythonOperator(
        task_id='transform_teams',
        python_callable=transform_teams
    )

    load = PythonOperator(
        task_id='load_teams',
        python_callable=load_teams
    )

extract >> transform >> load
