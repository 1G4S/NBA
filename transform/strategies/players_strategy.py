from extract.extract import Extract
from transform.strategies.abstract_strategy import Strategy


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
        """
        Retrieves players-specific data using the provided Extract instance.

        Parameters
        ----------
        extract : Extract
            An instance of the Extract class that is responsible for retrieving data.

        Returns
        -------
        DataFrame or relevant data structure
            The retrieved team-specific data, ready for further transformation or use.

        Notes
        -----
        The exact structure and type of the return value depend on how the `retrieve_specific_data`
        method in the `Extract` class is implemented.
        """
        return extract.retrieve_specific_data()
