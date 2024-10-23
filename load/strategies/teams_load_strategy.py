from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.teams_strategy import TeamsStrategy
from transform.transform import Transform


class TeamsLoadStrategy(LoadStrategy):
    def __init__(self):
        """
        Initializes the class and its components.

        Attributes:
            self.db_connection (str): The connection string for the PostgreSQL database.
            self.engine (object): The SQLAlchemy engine created using the database connection string.
            self.teams_retrieval_strategy (TeamsRetrievalStrategy): The strategy used for retrieving teams data.
            self.teams_extract (Extract): The extraction component initialized with the teams retrieval strategy.
            self.teams_strategy (TeamsStrategy): The strategy used for transforming teams data.
            self.transform (Transform): The transformation component initialized with the teams strategy and teams extract.
        """
        self.db_connection = 'postgresql+psycopg2://igorsarnowski:S3o3c3c3e3r3@localhost:5432/NBA'
        self.engine = create_engine(self.db_connection)
        self.teams_retrieval_strategy = TeamsRetrievalStrategy()
        self.teams_extract = Extract(self.teams_retrieval_strategy)
        self.teams_strategy = TeamsStrategy()
        self.transform = Transform(self.teams_strategy, self.teams_extract)

    def load(self):
        """
        Loads transformed data into the database.

        :return: None
        """
        df = self.transform.get_clean_data()
        df.to_sql("teams", con=self.engine, if_exists='replace')
