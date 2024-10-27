import os

from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy
from load.strategies.players_load_strategy import PlayersLoadStrategy
from load.load import Load
from load.strategies.stadiums_load_strategy import StadiumsLoadStrategy
from load.strategies.teams_load_strategy import TeamsLoadStrategy
from transform.strategies.players_strategy import PlayersStrategy
from transform.strategies.stadiums_strategy import StadiumsStrategy
from transform.strategies.teams_strategy import TeamsStrategy
from transform.transform import Transform
import json

#
# API_KEY = os.getenv('API_KEY', '')
# params = {
#     'api_key' :  os.getenv('API_KEY', '')
# }


'''
    extract:
        - strategy: get data from API -> list of JSONS or JSON 
        
    transform:
        - strategy: get json data

'''
def players():
    players_extract_strategy = PlayersRetrievalStrategy()
    players_extract = Extract(players_extract_strategy)
    players_json_message = players_extract.retrieve_specific_data()
    with open('data/players.json', 'w') as f:
        json.dump(players_json_message, f)
    players_transform_strategy = PlayersStrategy()
    players_transform = Transform(players_transform_strategy, players_extract)
    # players_transform.process_data(players_json_message)
    players_load_strategy = PlayersLoadStrategy(players_transform.get_clean_data())
    players_load = Load(players_load_strategy)
    players_load.load_prepared_data()


def teams():
    teams_extract_strategy = TeamsRetrievalStrategy()
    teams_extract = Extract(teams_extract_strategy)
    # save as json
    teams_json_message = teams_extract.retrieve_specific_data()
    with open('data/teams.json', 'w') as f:
        json.dump(teams_json_message, f)
    teams_transform_strategy = TeamsStrategy()
    teams_transform = Transform(teams_transform_strategy, teams_extract)
    teams_load_strategy = TeamsLoadStrategy(teams_transform.get_clean_data())
    teams_load = Load(teams_load_strategy)
    teams_load.load_prepared_data()


def stadiums():
    stadiums_extract_strategy = TeamsRetrievalStrategy()
    stadiums_extract = Extract(stadiums_extract_strategy)
    stadiums_json_message = stadiums_extract.retrieve_specific_data()
    with open('data/stadiums.json', 'w') as f:
        json.dump(stadiums_json_message, f)
    stadiums_transform_strategy = StadiumsStrategy()
    stadiums_transform = Transform(stadiums_transform_strategy, stadiums_extract)
    stadiums_load_strategy = StadiumsLoadStrategy(stadiums_transform.get_clean_data())
    stadiums_load = Load(stadiums_load_strategy)
    stadiums_load.load_prepared_data()


if __name__ == "__main__":
    # players()
    teams()
    stadiums()
