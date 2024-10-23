from sqlalchemy import create_engine

from extract.extract import Extract
from extract.strategies.stadiums_retrieval_strategy import StadiumsRetrievalStrategy
from load.strategies.abstract_load_strategy import LoadStrategy
from transform.strategies.stadiums_strategy import StadiumsStrategy
from transform.transform import Transform


class StadiumsLoadStrategy(LoadStrategy):
    def __init__(self):
        """
        Initializes the DatabaseHandler class with the necessary components for data extraction and transformation.

        Attributes:
            self.db_connection (str): The database connection string for PostgreSQL.
            self.engine (Engine): The SQLAlchemy engine instance for database interactions.
            self.stadiums_retrieval_strategy (StadiumsRetrievalStrategy): Strategy for retrieving stadium data.
            self.stadiums_extract (Extract): The extraction component configured with the specified retrieval strategy.
            self.stadiums_strategy (StadiumsStrategy): Strategy for transforming stadium data.
            self.transform (Transform): The transformation component configured with the specified strategy and
            extraction data.
        """
        self.db_connection = 'postgresql+psycopg2://igorsarnowski:S3o3c3c3e3r3@localhost:5432/NBA'
        self.engine = create_engine(self.db_connection)
        self.stadiums_retrieval_strategy = StadiumsRetrievalStrategy()
        self.stadiums_extract = Extract(self.stadiums_retrieval_strategy)
        self.stadiums_strategy = StadiumsStrategy()
        self.transform = Transform(self.stadiums_strategy, self.stadiums_extract)

    def load(self):
        """
        Loads transformed data into the database.

        :return: None
        """
        df = self.transform.get_clean_data()
        df.to_sql("stadiums", con=self.engine, if_exists='replace')