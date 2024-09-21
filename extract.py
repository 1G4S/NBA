import requests


class Extract:

    def __init__(self):
        self.API_KEY = "508f3dee654d4f5b8b06b9fe48bbb51e"
        self.ENDPOINT_MAIN = "https://api.sportsdata.io/v3/"
        self.endpoint_players = "nba/scores/json/Players"
        self.endpoint_stadiums = "nba/scores/json/Stadiums"
        self.endpoint_teams = "nba/scores/json/teams"
        self.teams = ["/WAS", "/CHA", "/ATL", "/MIA", "/ORL", "/NY", "/PHI", "/BKN", "/BOS",
                      "/TOR", "/CHI", "/CLE", "/IND", "/DET", "/MIL", "/MIN", "/UTA", "/OKC",
                      "/POR", "/DEN", "/MEM", "/HOU", "/NO", "/SA", "/DAL", "/GS", "/LAL", "/LAC",
                      "/PHO", "/SAC"]

    def get_teams(self):
        """
        Retrieves team data from the teams endpoint.

        This function constructs a URL using the base endpoint and the teams-specific
        endpoint, then sends a GET request with the API key as a parameter. It returns
        the data in JSON format.

        :param:
            None

        :return:
            dict: The JSON response containing team data.
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
            dict: The JSON response containing stadium data.
        """
        url = self.ENDPOINT_MAIN + self.endpoint_stadiums
        params = {'key': self.API_KEY}
        response = requests.get(url=url, params=params)
        return response.json()
