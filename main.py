from pprint import pprint

from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from transform.transform import Transform
from transform.strategies.players_strategy import PlayersStrategy

# extract = Extract()
# pprint(extract.get_players())
# pprint(extract.get_players()["CHA"])
# pprint(extract.get_stadiums())
# pprint(extract.get_teams())
# pprint(extract.get_players())
# stadiums = extract.get_stadiums()
# st = pd.DataFrame(stadiums)
# transform = Transform()
# pprint(transform.remove_columns(st, "Address", "GeoLat", "GeoLong", "Zip"))

# stadium_strategy = StadiumsStrategy()
# team_strategy = TeamsStrategy()
players_retrieval_strategy = PlayersRetrievalStrategy()
players_extract = Extract(players_retrieval_strategy)
player_strategy = PlayersStrategy()
transform7 = Transform(player_strategy, players_extract)
pprint(transform7.get_clean_data())
