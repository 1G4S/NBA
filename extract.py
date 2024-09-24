import json

import requests


class Extract:

    def __init__(self):
        self.API_KEY = "508f3dee654d4f5b8b06b9fe48bbb51e"
        self.ENDPOINT_MAIN = "https://api.sportsdata.io/v3/"
        self.endpoint_players = "nba/scores/json/Players"
        self.endpoint_stadiums = "nba/scores/json/Stadiums"
        self.endpoint_teams = "nba/scores/json/teams"
        self.filename = 'teams.json'
        self.session = requests.Session()

    def get_teams(self):
        """
        Retrieves team data from the teams endpoint.

        This function constructs a URL using the base endpoint and the teams-specific
        endpoint, then sends a GET request with the API key as a parameter. It returns
        the data in JSON format.

        :param:
            None

        :return:
            list: The JSON response containing team data.
        """
        url = self.ENDPOINT_MAIN + self.endpoint_teams
        params = {'key': self.API_KEY}
        response = requests.get(url=url, params=params)
        return response.json()

    def get_stadiums(self):
        """
        Retrieves stadium data from stadium endpoint.

        This function constructs URL using the base endpoint and the stadium-specific
        endpoint, then sends a GET request with the API key as a parameter. It returns
        the data in JSON format.

        :param:
            None

        :return:
            list: The JSON response containing stadium data.
        """
        url = self.ENDPOINT_MAIN + self.endpoint_stadiums
        params = {'key': self.API_KEY}
        response = requests.get(url=url, params=params)
        return response.json()

    def get_players(self):
        """
        Retrieves players data from players endpoint.

        This function constructs URL using the base endpoint, the players-specific
        endpoint and the team specific shortcut. It also uses for loop to get all players for each team.
        Then sends a GET request with the API key as a parameter.
        It returns the data in JSON format and then put into dict.

        :param:
            None

        :return:
            dict: The JSON response containing players data for each team.
        """
        all_players = {}
        for team in self.get_list_of_teams():
            url = self.ENDPOINT_MAIN + self.endpoint_players + "/" + team
            params = {'key': self.API_KEY}
            response = self.session.get(url=url, params=params)
            all_players[team] = response.json()

        return all_players

    def get_list_of_teams(self):
        """
        Get list of teams from json file.

        This function read data from json file and returns list of teams
        from NBA.
        :return:
            list: List of teams from NBA.
        """
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data['Teams']
