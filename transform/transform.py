from __future__ import annotations
import pandas as pd
from transform.strategies.abstract_transform_strategy import Strategy


class Transform:
    def __init__(self, strategy: Strategy):
        """
        :param strategy: An instance of the Strategy class that defines the algorithm to be used.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        :return: The current strategy object, representing the approach or algorithm to be used in a certain context.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        :param strategy: The strategy instance to be set.
        :return: None
        """
        self._strategy = strategy

    def get_clean_data(self):
        """
        :return: A cleaned pandas DataFrame with unnecessary columns removed
        """
        data_in_dataframe = self.normalize_to_pandas()
        return self.delete_columns(data_in_dataframe)

    def delete_columns(self, dataframe):
        """
        :param dataframe: DataFrame from which columns need to be removed.
        :return: DataFrame with specified columns removed.
        """
        return dataframe.drop(columns=self._strategy.list_of_columns_to_remove)

    def normalize_to_pandas(self):
        """
        Transforms raw data from the strategy to a pandas DataFrame.

        :return: A pandas DataFrame containing the strategy's raw data.
        """
        data = self._strategy.raw_data
        return pd.DataFrame(data)
