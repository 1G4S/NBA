import datetime
import os
from dotenv import load_dotenv

from airflow import DAG
from airflow.operators.python import PythonOperator

from extract.extract import Extract
from transform.transform import Transform
from load.load import Load

from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from transform.strategies.players_transform_strategy import PlayersTransformStrategy
from load.strategies.players_load_strategy import PlayersLoadStrategy

load_dotenv()

API_KEY = os.getenv('API_KEY')
ENDPOINT_MAIN = os.getenv('ENDPOINT_MAIN')
ENDPOINT_PLAYERS = os.getenv('ENDPOINT_PLAYERS')
ENDPOINT_TEAMS = os.getenv('ENDPOINT_TEAMS')
ENDPOINT_STADIUMS = os.getenv('ENDPOINT_STADIUMS')
DB_CONNECTION = os.getenv('DB_CONNECTION')
"""
 * * * * *

 - minuta (0 -59)
 - godizna (0 - 23)
 - dzien miesiaca (1 - 31)
 - miesiac (1-12)
 - dzien tygodnia (0 - 7)

 0 0 * * * -> every day
 */5 * * * * -> every 5 min

"""


def extract_players(**kwargs):
    ''' wrapper for extract players data '''
    print('Current dir: ', os.getcwd())
    players_extract_strategy = PlayersRetrievalStrategy(
        api_key=API_KEY,
        endpoint_main=ENDPOINT_MAIN,
        endpoint_players=ENDPOINT_PLAYERS
    )
    players_extract = Extract(players_extract_strategy)
    kwargs['ti'].xcom_push(
        key='players_raw_data',
        value=players_extract.save_data()
    )


def transform_players(**kwargs):
    ''' wrapper for tranform players data '''
    file_path = kwargs['ti'].xcom_pull(
        task_ids='extract_players',
        key='players_raw_data'
    )
    players_transform_strategy = PlayersTransformStrategy(
        path_to_data=file_path
    )
    players_transform = Transform(players_transform_strategy)

    kwargs['ti'].xcom_push(key='players_prepared_data',
                           value=players_transform.get_clean_data())


def load_players(**kwargs):
    players_prepared_data = kwargs['ti'].xcom_pull(
        task_ids='transform_players',
        key='players_prepared_data'
    )
    players_load_strategy = PlayersLoadStrategy(players_prepared_data, DB_CONNECTION)
    players_load = Load(players_load_strategy)
    players_load.load_prepared_data()


default_args = {
    'owner': 'admin',
    'start_date': datetime.datetime(2024, 11, 26),
    'retries': 0,
}

with DAG(
        dag_id='players_dag',
        default_args=default_args,
        schedule_interval='@daily',
) as dag:
    extract = PythonOperator(
        task_id='extract_players',
        python_callable=extract_players
    )

    transform = PythonOperator(
        task_id='transform_players',
        python_callable=transform_players
    )

    load = PythonOperator(
        task_id='load_players',
        python_callable=load_players
    )

extract >> transform >> load
