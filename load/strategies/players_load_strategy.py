from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.players_strategy import PlayersStrategy
from transform.transform import Transform


class PlayersLoadStrategy(LoadStrategy):
    def __init__(self, prepared_data):
        """
        :param prepared_data: Prepared data to be stored or processed.
        """
        self.db_connection = 'postgresql+psycopg2://igorsarnowski:S3o3c3c3e3r3@localhost:5432/NBA'
        self.engine = create_engine(self.db_connection)
        self.prepared_data = prepared_data

    def load(self):
        """
        Loads transformed data into the database.

        :return: None
        """
        df = self.prepared_data
        df.to_sql("players", con=self.engine, if_exists='replace')
