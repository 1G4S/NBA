import os

import requests
from dotenv import load_dotenv
from requests import RequestException

from extract.strategies.abstract_extract_strategy import ExtractStrategy


class TeamsRetrievalStrategy(ExtractStrategy):
    def __init__(self, api_key, endpoint_main, endpoint_teams):
        self.API_KEY = api_key
        self.ENDPOINT_MAIN = endpoint_main
        self.ENDPOINT_TEAMS = endpoint_teams
        self.dest_path = f'{os.getcwd()}/dags/data/teams.json'

    def get_dest_path(self):
        return self.dest_path

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
