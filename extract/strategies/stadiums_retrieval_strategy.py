import requests
from requests import RequestException

from extract.strategies.abstract_strategy import ExtractStrategy


class StadiumsRetrievalStrategy(ExtractStrategy):
    def __init__(self):
        self.API_KEY = "508f3dee654d4f5b8b06b9fe48bbb51e"
        self.ENDPOINT_MAIN = "https://api.sportsdata.io/v3/"
        self.ENDPOINT_STADIUMS = "nba/scores/json/Stadiums"

    def retrieve_data(self):
        """
        Retrieves stadium data from stadium endpoint.

        This function constructs URL using the base endpoint and the stadium-specific
        endpoint, then sends a GET request with the API key as a parameter. It returns
        the data in JSON format if the request is successful, if not there will be None returned.

        :param:
            None

        :return:
            list: The JSON response containing stadium data.
        """
        url = self.ENDPOINT_MAIN + self.ENDPOINT_STADIUMS
        params = {'key': self.API_KEY}
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching stadium data: {e}")
            return None
