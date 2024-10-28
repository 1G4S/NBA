from extract.extract import Extract
from transform.strategies.abstract_transform_strategy import TransformStrategy


class TeamsTransformStrategy(TransformStrategy):
    def __init__(self, raw_data):
        """
        :param raw_data: The raw input data that needs processing. This could be in various formats,
                         but it should be consistent with what the class methods expect.
        """
        self.list_of_columns_to_remove = ['GlobalTeamID', 'LeagueID', 'NbaDotComTeamID', 'PrimaryColor',
                                          'QuaternaryColor', 'SecondaryColor', 'TertiaryColor', 'WikipediaLogoUrl',
                                          'WikipediaWordMarkUrl']
        self.raw_data = raw_data

    def get_data(self):
        """
        :return: The raw_data attribute of the instance.
        """
        return self.raw_data
