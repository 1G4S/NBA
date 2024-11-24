import requests
import json
from requests import RequestException
from extract.strategies.abstract_extract_strategy import ExtractStrategy


class PlayersRetrievalStrategy(ExtractStrategy):
    def __init__(self, api_key, endpoint_main, endpoint_players, filename='teams.json'):
        self.API_KEY = api_key
        self.ENDPOINT_MAIN = endpoint_main
        self.ENDPOINT_PLAYERS = endpoint_players
        self.session = requests.Session()
        self.filename = filename

    def retrieve_data(self):
        """
        Retrieves players data from players endpoint.

        This function constructs the URL by combining the base endpoint, the players-specific
        endpoint, and the team-specific shortcut for each team. It uses a for loop to send a GET request
        for each team with the API key as a parameter and collects the players' data.
        If a request is successful, the JSON response is parsed and added to a list.
        In case of a request or JSON parsing error,
        the team entry will have a value of None.

        :param:
            None

        :return:
            list: The JSON response containing players data for each team.
        """
        all_players = []
        for team in self.get_list_of_teams():
            url = self.ENDPOINT_MAIN + self.ENDPOINT_PLAYERS + "/" + team
            params = {'key': self.API_KEY}
            try:
                response = self.session.get(url=url, params=params)
                response.raise_for_status()
                all_players.extend(response.json())

            except RequestException as e:
                print(f"Error fetching fata for {team}: {e}")
                all_players = None

        return all_players

    def get_list_of_teams(self):
        """
        Get list of teams from json file.

        This function read data from json file and returns list of teams
        from NBA, if loading data is successful, if not, None will be returned.
        :return:
            list: List of teams from NBA.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data['Teams']
        except Exception as e:
            print(e)
            return None
