from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.teams_transform_strategy import TeamsTransformStrategy
from transform.transform import Transform


class TeamsLoadStrategy(LoadStrategy):
    def __init__(self, prepared_data, db_connection):
        """
        :param prepared_data: Preprocessed data that will be used for database operations
        :type prepared_data: dict
        :param db_connection: Database connection string
        :type db_connection: str
        """
        self.db_connection = db_connection
        self.engine = create_engine(self.db_connection)
        self.prepared_data = prepared_data

    def load(self):
        """
        Loads the prepared data into a SQL database, replacing the existing data in the "teams" table.

        :return: None
        """
        df = self.prepared_data
        df.to_sql("teams", con=self.engine, if_exists='replace')
