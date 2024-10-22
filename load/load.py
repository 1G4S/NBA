from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from extract.strategies.stadiums_retrieval_strategy import StadiumsRetrievalStrategy
from transform.strategies.players_strategy import PlayersStrategy
from transform.strategies.stadiums_strategy import StadiumsStrategy
from transform.transform import Transform

connection_string = 'postgresql+psycopg2://igorsarnowski:S3o3c3c3e3r3@localhost:5432/NBA'
engine = create_engine(connection_string)

stadiums_retrieval_strategy = StadiumsRetrievalStrategy()
stadiums_extract = Extract(stadiums_retrieval_strategy)
stadiums_strategy = StadiumsStrategy()
transform1 = Transform(stadiums_strategy, stadiums_extract)

players_retrieval_strategy = PlayersRetrievalStrategy()
players_extract = Extract(players_retrieval_strategy)
players_strategy = PlayersStrategy()
transform2 = Transform(players_strategy, players_extract)

df1 = transform1.get_clean_data()
df2 = transform2.get_clean_data()
df1.to_sql("stadiums", con=engine, if_exists='replace')
df2.to_sql("players", con=engine, if_exists='replace')

# general conn function -> create_connection_engine -> param: (postgres, mysql, mssql) -> conn_string -> engine
# load -> param: engine -> exec to_sql -> end
