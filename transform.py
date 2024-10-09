from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from extract import Extract


class Transform:
    """
    1. Data Cleaning -> remove unnecessary columns
    2. Split process to 3 endpoints: players, teams, stadiums
    3. Create general functions for all 3 processes
    4. Create Relational database diagram via Normalization
    """

    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        self.extract = Extract()

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
        """ """
        return dataframe.drop(columns=self._strategy.list_of_columns_to_remove)

    def normalize_to_pandas(self):
        data = self._strategy.get_data(self.extract)
        return pd.DataFrame(data)


class Strategy(ABC):

    @abstractmethod
    def get_data(self, extract: Extract):
        pass


class StadiumsStrategy(Strategy):
    def __init__(self):
        self.list_of_columns_to_remove = ['Address', 'GeoLat', 'GeoLong', 'Zip']

    def get_data(self, extract: Extract):
        return extract.get_stadiums()


class TeamsStrategy(Strategy):
    def __init__(self):
        self.list_of_columns_to_remove = ['GlobalTeamID', 'LeagueID', 'NbaDotComTeamID', 'PrimaryColor',
                                          'QuaternaryColor', 'SecondaryColor', 'TertiaryColor', 'WikipediaLogoUrl',
                                          'WikipediaWordMarkUrl']

    def get_data(self, extract: Extract):
        return extract.get_teams()


class PlayersStrategy(Strategy):
    def __init__(self):
        self.list_of_columns_to_remove = ['BirthCountry', 'BirthState', 'College', 'DepthChartOrder',
                                          'DepthChartPosition', 'DraftKingsName', 'DraftKingsPlayerID', 'Experience',
                                          'FanDuelName', 'FanDuelPlayerID', 'FantasyAlarmPlayerID', 'FantasyDraftName',
                                          'FantasyDraftPlayerID', 'GlobalTeamID', 'HighSchool', 'InjuryBodyPart',
                                          'InjuryNotes', 'InjuryStartDate', 'InjuryStatus', 'Jersey',
                                          'NbaDotComPlayerID', 'PhotoUrl', 'PositionCategory', 'RotoWirePlayerID',
                                          'RotoworldPlayerID', 'SportRadarPlayerID', 'SportsDataID',
                                          'SportsDirectPlayerID', 'StatsPlayerID', 'Status',
                                          'UsaTodayHeadshotNoBackgroundUpdated', 'UsaTodayHeadshotNoBackgroundUrl',
                                          'UsaTodayHeadshotUpdated', 'UsaTodayHeadshotUrl', 'UsaTodayPlayerID',
                                          'XmlTeamPlayerID', 'YahooName', 'YahooPlayerID']

    def get_data(self, extract: Extract):
        return extract.get_players()
