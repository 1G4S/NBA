from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy
from load.strategies.players_load_strategy import PlayersLoadStrategy
from load.load import Load
from load.strategies.stadiums_load_strategy import StadiumsLoadStrategy
from load.strategies.teams_load_strategy import TeamsLoadStrategy
from transform.strategies.players_strategy import PlayersStrategy
from transform.transform import Transform


def players():
    players_extract_strategy = PlayersRetrievalStrategy()
    players_extract = Extract(players_extract_strategy)
    players_transform_strategy = PlayersStrategy()
    players_transform = Transform(players_transform_strategy, players_extract)
    players_load_strategy = PlayersLoadStrategy(players_transform.get_clean_data())
    players_load = Load(players_load_strategy)
    players_load.load_prepared_data()


def teams():
    teams_extract_strategy = TeamsRetrievalStrategy()
    teams_extract = Extract(teams_extract_strategy)
    teams_transform_strategy = PlayersStrategy()
    teams_transform = Transform(teams_transform_strategy, teams_extract)
    teams_load_strategy = TeamsLoadStrategy(teams_transform.get_clean_data())
    teams_load = Load(teams_load_strategy)
    teams_load.load_prepared_data()


def stadiums():
    stadiums_extract_strategy = TeamsRetrievalStrategy()
    stadiums_extract = Extract(stadiums_extract_strategy)
    stadiums_transform_strategy = PlayersStrategy()
    stadiums_transform = Transform(stadiums_transform_strategy, stadiums_extract)
    stadiums_load_strategy = StadiumsLoadStrategy(stadiums_transform.get_clean_data())
    stadiums_load = Load(stadiums_load_strategy)
    stadiums_load.load_prepared_data()


if __name__ == "__main__":
    players()
    teams()
    stadiums()
