from load.strategies.players_load_strategy import PlayersLoadStrategy
from load.load import Load
from load.strategies.stadiums_load_strategy import StadiumsLoadStrategy
from load.strategies.teams_load_strategy import TeamsLoadStrategy

players_load_strategy = PlayersLoadStrategy()
players_load = Load(players_load_strategy)
players_load.load_prepared_data()

teams_load_strategy = TeamsLoadStrategy()
teams_load = Load(teams_load_strategy)
teams_load.load_prepared_data()

stadiums_load_strategy = StadiumsLoadStrategy()
stadiums_load = Load(stadiums_load_strategy)
stadiums_load.load_prepared_data()
