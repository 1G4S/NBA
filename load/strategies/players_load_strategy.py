from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.players_strategy import PlayersStrategy
from transform.transform import Transform


class PlayersLoadStrategy(LoadStrategy):
    def __init__(self):
        """
        Initializes a new instance of the class.

        Attributes:
            self.db_connection (str): The connection string for the PostgreSQL database.
            self.engine (Engine): The SQLAlchemy engine created with the database connection.
            self.players_retrieval_strategy (PlayersRetrievalStrategy): Strategy for retrieving players.
            self.players_extract (Extract): An instance of Extract class to extract player information.
            self.players_strategy (PlayersStrategy): Strategy for processing player-related data.
            self.transform (Transform): An instance of Transform class to handle data transformation.
        """
        self.db_connection = 'postgresql+psycopg2://igorsarnowski:S3o3c3c3e3r3@localhost:5432/NBA'
        self.engine = create_engine(self.db_connection)
        self.players_retrieval_strategy = PlayersRetrievalStrategy()
        self.players_extract = Extract(self.players_retrieval_strategy)
        self.players_strategy = PlayersStrategy()
        self.transform = Transform(self.players_strategy, self.players_extract)

    def load(self):
        """
        Loads transformed data into the database.

        :return: None
        """
        df = self.transform.get_clean_data()
        df.to_sql("players", con=self.engine, if_exists='replace')
