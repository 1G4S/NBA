from extract.extract import Extract
from transform.strategies.abstract_transform_strategy import TransformStrategy
import pandas as pd


class TeamsTransformStrategy(TransformStrategy):
    def __init__(self, path_to_data):
        """
        :param raw_data: The raw input data that needs processing. This could be in various formats,
                         but it should be consistent with what the class methods expect.
        """
        self.list_of_columns_to_remove = ['GlobalTeamID', 'LeagueID', 'NbaDotComTeamID', 'PrimaryColor',
                                          'QuaternaryColor', 'SecondaryColor', 'TertiaryColor', 'WikipediaLogoUrl',
                                          'WikipediaWordMarkUrl']
        self.path_to_data = path_to_data

    def get_data(self):
        """
        :return: Reading data from json file.
        """
        return pd.read_json(self.path_to_data)
