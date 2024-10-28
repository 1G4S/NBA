from transform.strategies.abstract_transform_strategy import TransformStrategy


class StadiumsTransformStrategy(TransformStrategy):
    def __init__(self, raw_data):
        """
        :param raw_data: The initial data that needs to be processed, typically in a tabular or dataframe format.
        """
        self.list_of_columns_to_remove = ['Address', 'GeoLat', 'GeoLong', 'Zip']
        self.raw_data = raw_data

    def get_data(self):
        """
        :return: The raw data stored within the object.
        """
        return self.raw_data
