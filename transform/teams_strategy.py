from extract.extract import Extract
from transform.transform_strategy import Strategy


class TeamsStrategy(Strategy):
    def __init__(self):
        self.list_of_columns_to_remove = ['GlobalTeamID', 'LeagueID', 'NbaDotComTeamID', 'PrimaryColor',
                                          'QuaternaryColor', 'SecondaryColor', 'TertiaryColor', 'WikipediaLogoUrl',
                                          'WikipediaWordMarkUrl']

    def get_data(self, extract: Extract):
        return extract.get_teams()
