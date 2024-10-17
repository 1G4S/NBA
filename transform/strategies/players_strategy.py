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
        return extract.retrieve_specific_data()
