import json

import requests
from requests import RequestException


class Extract:

    def __init__(self, filename='teams.json'):
        self.API_KEY = "508f3dee654d4f5b8b06b9fe48bbb51e"
        self.ENDPOINT_MAIN = "https://api.sportsdata.io/v3/"
        self.endpoint_players = "nba/scores/json/Players"
        self.endpoint_stadiums = "nba/scores/json/Stadiums"
        self.endpoint_teams = "nba/scores/json/teams"
        self.filename = filename
        self.session = requests.Session()

    def get_teams(self):
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
        url = self.ENDPOINT_MAIN + self.endpoint_teams
        params = {'key': self.API_KEY}
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching teams data: {e}")
            return None

    def get_stadiums(self):
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
        url = self.ENDPOINT_MAIN + self.endpoint_stadiums
        params = {'key': self.API_KEY}
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching stadium data: {e}")
            return None
    #
    # def get_players(self):
    #     """
    #     Retrieves players data from players endpoint.
    #
    #     This function constructs the URL by combining the base endpoint, the players-specific
    #     endpoint, and the team-specific shortcut for each team. It uses a for loop to send a GET request
    #     for each team with the API key as a parameter and collects the players' data.
    #     If a request is successful, the JSON response is parsed and added to a list.
    #     In case of a request or JSON parsing error,
    #     the team entry will have a value of None.
    #
    #     :param:
    #         None
    #
    #     :return:
    #         list: The JSON response containing players data for each team.
    #     """
    #     all_players = []
    #     for team in self.get_list_of_teams():
    #         url = self.ENDPOINT_MAIN + self.endpoint_players + "/" + team
    #         params = {'key': self.API_KEY}
    #         try:
    #             response = self.session.get(url=url, params=params)
    #             response.raise_for_status()
    #             all_players.extend(response.json())
    #
    #         except RequestException as e:
    #             print(f"Error fetching fata for {team}: {e}")
    #             all_players = None
    #
    #     return all_players
    #
    # def get_list_of_teams(self):
    #     """
    #     Get list of teams from json file.
    #
    #     This function read data from json file and returns list of teams
    #     from NBA, if loading data is successful, if not, None will be returned.
    #     :return:
    #         list: List of teams from NBA.
    #     """
    #     try:
    #         with open(self.filename, 'r') as file:
    #             data = json.load(file)
    #             return data['Teams']
    #     except Exception as e:
    #         print(e)
    #         return None
    #
