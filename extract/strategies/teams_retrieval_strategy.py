import requests
from requests import RequestException

from extract.strategies.abstract_strategy import ExtractStrategy


class TeamsRetrievalStrategy(ExtractStrategy):
    def __init__(self):
        self.API_KEY = "508f3dee654d4f5b8b06b9fe48bbb51e"
        self.ENDPOINT_MAIN = "https://api.sportsdata.io/v3/"
        self.ENDPOINT_TEAMS = "nba/scores/json/teams"

    def retrieve_data(self):
        """
        Retrieves team data from the teams endpoint.

        This function constructs a URL using the base endpoint and the teams-specific
        endpoint, then sends a GET request with the API key as a parameter. It returns
        the data in JSON format if request is successful, if not, None will be returned.

        :param:
            None

        :return:
            list: The JSON response containing team data.
        """
        url = self.ENDPOINT_MAIN + self.ENDPOINT_TEAMS
        params = {'key': self.API_KEY}
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching teams data: {e}")
            return None
