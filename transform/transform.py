from __future__ import annotations
import pandas as pd
from extract.extract import Extract
from transform.strategies.abstract_strategy import Strategy


class Transform:
    def __init__(self, strategy: Strategy, extract: Extract):
        """
        Initialize the Transform class.

        Parameters:
        strategy (Strategy): The strategy for transforming data.
        extract (Extract): The extractor instance to retrieve raw data.
        """
        self._strategy = strategy
        self.extract = extract

    @property
    def strategy(self) -> Strategy:
        """
        Get the current transformation strategy.

        Returns:
        Strategy: The current strategy instance used for data transformation.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Set a new transformation strategy.

        Parameters:
        strategy (Strategy): The new strategy instance for transforming data.
        """
        self._strategy = strategy

    def get_clean_data(self):
        """
        Retrieve and clean the data by normalizing it and removing unnecessary columns.

        Returns:
        pd.DataFrame: A cleaned DataFrame with unnecessary columns removed.
        """
        data_in_dataframe = self.normalize_to_pandas()
        return self.delete_columns(data_in_dataframe)

    def delete_columns(self, dataframe):
        """
        Remove specified columns from the DataFrame based on the strategy.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame from which columns will be removed.

        Returns:
        pd.DataFrame: The DataFrame with the specified columns removed.
        """
        return dataframe.drop(columns=self._strategy.list_of_columns_to_remove)

    def normalize_to_pandas(self):
        """
        Normalize the data retrieved by the strategy into a Pandas DataFrame.

        Returns:
        pd.DataFrame: A DataFrame containing the normalized data.
        """
        data = self._strategy.get_data(self.extract)
        return pd.DataFrame(data)
