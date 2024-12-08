from transform.strategies.abstract_transform_strategy import TransformStrategy
import pandas as pd


class StadiumsTransformStrategy(TransformStrategy):
    def __init__(self, path_to_data):
        """
        :param path_to_data: The initial data that needs to be processed, typically in a tabular or dataframe format.
        """
        self.list_of_columns_to_remove = ['Address', 'GeoLat', 'GeoLong', 'Zip']
        self.path_to_data = path_to_data

    def get_data(self):
        """
        :return: Reading raw data stored in json file.
        """
        return pd.read_json(self.path_to_data)
