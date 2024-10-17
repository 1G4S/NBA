from __future__ import annotations
import pandas as pd
from extract.extract import Extract
from transform.strategies.abstract_strategy import Strategy


class Transform:
    """
    1. Data Cleaning -> remove unnecessary columns
    2. Split process to 3 endpoints: players, teams, stadiums
    3. Create general functions for all 3 processes
    4. Create Relational database diagram via Normalization
    """

    def __init__(self, strategy: Strategy, extract: Extract):
        self._strategy = strategy
        self.extract = extract

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_clean_data(self):
        data_in_dataframe = self.normalize_to_pandas()
        return self.delete_columns(data_in_dataframe)

    def delete_columns(self, dataframe):
        return dataframe.drop(columns=self._strategy.list_of_columns_to_remove)

    def normalize_to_pandas(self):
        data = self._strategy.get_data(self.extract)
        return pd.DataFrame(data)
