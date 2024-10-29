import os

from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.players_transform_strategy import PlayersTransformStrategy
from transform.transform import Transform


class PlayersLoadStrategy(LoadStrategy):
    def __init__(self, prepared_data, db_connection):
        """
        :param prepared_data: The data that has been pre-processed and is ready for insertion into the database.
        :type prepared_data: Any

        :param db_connection: The database connection string used to establish a connection to the database.
        :type db_connection: str
        """
        self.db_connection = db_connection
        self.engine = create_engine(self.db_connection)
        self.prepared_data = prepared_data

    def load(self):
        """
        Writes the prepared DataFrame to a SQL database table named 'players'.

        :return: None
        """
        df = self.prepared_data
        df.to_sql("players", con=self.engine, if_exists='replace')
