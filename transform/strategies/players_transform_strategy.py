from transform.strategies.abstract_transform_strategy import TransformStrategy


class PlayersTransformStrategy(TransformStrategy):
    def __init__(self, raw_data):
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
        self.raw_data = raw_data

    def get_data(self):
        """
        This method retrieves the data stored in the instance variable.

        :return: The data stored in the instance variable.
        """
        return self.raw_data
