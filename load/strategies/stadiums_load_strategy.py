from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.stadiums_retrieval_strategy import StadiumsRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.stadiums_transform_strategy import StadiumsTransformStrategy
from transform.transform import Transform


class StadiumsLoadStrategy(LoadStrategy):
    def __init__(self, prepared_data, db_connection):
        """
        :param prepared_data: The data that has been processed and is ready for use by the application.
        :type prepared_data: dict
        :param db_connection: The database connection string used to connect to the database.
        :type db_connection: str
        """
        self.db_connection = db_connection
        self.engine = create_engine(self.db_connection)
        self.prepared_data = prepared_data

    def load(self):
        """
        Loads the prepared DataFrame into a SQL table named 'stadiums'. If the table already exists, it will be replaced.

        :param df: DataFrame containing the prepared data
        """
        df = self.prepared_data
        df.to_sql("stadiums", con=self.engine, if_exists='replace')
