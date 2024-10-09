import json

import requests
import pandas as pd
from extract import Extract
from pprint import pprint

from transform import Transform, StadiumsStrategy, TeamsStrategy, PlayersStrategy

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
player_strategy = PlayersStrategy()
transform = Transform(player_strategy)
pprint(transform.get_clean_data())
