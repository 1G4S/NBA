from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime as dt

from dotenv import load_dotenv
from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from extract.strategies.stadiums_retrieval_strategy import StadiumsRetrievalStrategy
from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy
from load.strategies.players_load_strategy import PlayersLoadStrategy
from load.load import Load
from load.strategies.stadiums_load_strategy import StadiumsLoadStrategy
from load.strategies.teams_load_strategy import TeamsLoadStrategy
from transform.strategies.players_transform_strategy import PlayersTransformStrategy
from transform.strategies.stadiums_transform_strategy import StadiumsTransformStrategy
from transform.strategies.teams_transform_strategy import TeamsTransformStrategy
from transform.transform import Transform
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
ENDPOINT_MAIN = os.getenv('ENDPOINT_MAIN')
ENDPOINT_PLAYERS = os.getenv('ENDPOINT_PLAYERS')
ENDPOINT_TEAMS = os.getenv('ENDPOINT_TEAMS')
ENDPOINT_STADIUMS = os.getenv('ENDPOINT_STADIUMS')
DB_CONNECTION = os.getenv('DB_CONNECTION')

players_extract_strategy = PlayersRetrievalStrategy(
    api_key=API_KEY,
    endpoint_main=ENDPOINT_MAIN,
    endpoint_players=ENDPOINT_PLAYERS
)
players_extract = Extract(players_extract_strategy)


players_transform_strategy = PlayersTransformStrategy(players_raw_data)
players_transform = Transform(players_transform_strategy)
players_prepared_data = players_transform.get_clean_data()
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

default_args1 = {
    'owner': 'admin',
    'start_date': dt.datetime.date(),
    'retries': 0,
}

with DAG(
    dag_id='test_dag',
    default_args=default_args1,
    schedule_interval='@daily'
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=players_extract.retrieve_specific_data()
    )

    raw_data = xcom_p



