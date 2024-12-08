from transform.strategies.abstract_transform_strategy import TransformStrategy
import pandas as pd

class PlayersTransformStrategy(TransformStrategy):
    def __init__(self, path_to_data):
        """
        :param raw_data: The dataset that contains player information which will be cleaned by removing unnecessary
        columns.
        """
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
        self.path_to_data = path_to_data

    def get_data(self):
        """
        This method retrieves the data stored in the instance variable.

        :return: The data stored in the instance variable.
        """

        return pd.read_json(self.path_to_data)
