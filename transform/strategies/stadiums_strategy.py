from extract.extract import Extract
from transform.strategies.abstract_strategy import Strategy


class StadiumsStrategy(Strategy):
    def __init__(self):
        self.list_of_columns_to_remove = ['Address', 'GeoLat', 'GeoLong', 'Zip']

    def get_data(self, extract: Extract):
        return extract.retrieve_specific_data()
