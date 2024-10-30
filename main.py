import os

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
import json

load_dotenv()
API_KEY = os.getenv('API_KEY')
ENDPOINT_MAIN = os.getenv('ENDPOINT_MAIN')
ENDPOINT_PLAYERS = os.getenv('ENDPOINT_PLAYERS')
ENDPOINT_TEAMS = os.getenv('ENDPOINT_TEAMS')
ENDPOINT_STADIUMS = os.getenv('ENDPOINT_STADIUMS')
DB_CONNECTION = os.getenv('DB_CONNECTION')


def players():
    # ----------------START EXTRACT--------------------#
    players_extract_strategy = PlayersRetrievalStrategy(api_key=API_KEY, endpoint_main=ENDPOINT_MAIN,
                                                        endpoint_players=ENDPOINT_PLAYERS)
    players_extract = Extract(players_extract_strategy)
    # players_json_message = players_extract.retrieve_specific_data()
    # with open('data/players.json', 'w') as f:
    #     json.dump(players_json_message, f)
    players_raw_data = players_extract.retrieve_specific_data()
    # ----------------END OF EXTRACT--------------------#

    # ----------------START TRANSFORM-------------------#
    players_transform_strategy = PlayersTransformStrategy(players_raw_data)
    players_transform = Transform(players_transform_strategy)
    players_prepared_data = players_transform.get_clean_data()
    # ----------------END TRANSFORM-------------------#

    # -----------------START LOAD----------------------#
    players_load_strategy = PlayersLoadStrategy(players_prepared_data, DB_CONNECTION)
    players_load = Load(players_load_strategy)
    players_load.load_prepared_data()
    # -----------------END LOAD----------------------#


def teams():
    # ----------------START EXTRACT--------------------#
    teams_extract_strategy = TeamsRetrievalStrategy(api_key=API_KEY, endpoint_main=ENDPOINT_MAIN,
                                                    endpoint_teams=ENDPOINT_TEAMS)
    teams_extract = Extract(teams_extract_strategy)
    # save as json
    # teams_json_message = teams_extract.retrieve_specific_data()
    # with open('data/teams.json', 'w') as f:
    #     json.dump(teams_json_message, f)
    # ----------------END OF EXTRACT--------------------#
    # ----------------START TRANSFORM-------------------#
    teams_raw_data = teams_extract.retrieve_specific_data()
    # ----------------END OF EXTRACT--------------------#

    # ----------------START TRANSFORM-------------------#
    teams_transform_strategy = TeamsTransformStrategy(teams_raw_data)
    teams_transform = Transform(teams_transform_strategy)
    team_prepared_data = teams_transform.get_clean_data()
    # ----------------END TRANSFORM-------------------#

    # -----------------START LOAD----------------------#
    teams_load_strategy = TeamsLoadStrategy(team_prepared_data, DB_CONNECTION)
    teams_load = Load(teams_load_strategy)
    teams_load.load_prepared_data()
    # -----------------END LOAD----------------------#


def stadiums():
    # ----------------START EXTRACT--------------------#
    stadiums_extract_strategy = StadiumsRetrievalStrategy(api_key=API_KEY, endpoint_main=ENDPOINT_MAIN,
                                                          endpoint_stadiums=ENDPOINT_STADIUMS)
    stadiums_extract = Extract(stadiums_extract_strategy)
    # stadiums_json_message = stadiums_extract.retrieve_specific_data()
    # # with open('data/stadiums.json', 'w') as f:
    # #     json.dump(stadiums_json_message, f)
    stadiums_raw_data = stadiums_extract.retrieve_specific_data()
    # ----------------END OF EXTRACT--------------------#

    # ----------------START TRANSFORM-------------------#
    stadiums_transform_strategy = StadiumsTransformStrategy(stadiums_raw_data)
    stadiums_transform = Transform(stadiums_transform_strategy)
    stadiums_prepared_data = stadiums_transform.get_clean_data()
    # ----------------END TRANSFORM-------------------#

    # -----------------START LOAD----------------------#
    stadiums_load_strategy = StadiumsLoadStrategy(stadiums_prepared_data, DB_CONNECTION)
    stadiums_load = Load(stadiums_load_strategy)
    stadiums_load.load_prepared_data()
    # -----------------END LOAD----------------------#


if __name__ == "__main__":
    # players()
    teams()
    # stadiums()
