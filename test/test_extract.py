import unittest
from unittest.mock import patch, Mock

from extract import Extract


class TestExtractFunctions(unittest.TestCase):
    @patch('requests.get')
    def test_get_teams(self, mock_get):
        """
        Tests the get_teams method to ensure it correctly fetches team data from the API.

        Mocks the requests.get call to simulate an API response and verifies that the
        get_teams method returns the expected JSON data without making an actual API call.

        :param mock_get:
            A mock object that simulates the requests.get method.

        """
        mock_response = {'teams': []}

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response

        extract = Extract(filename="../teams.json")
        result = extract.get_teams()

        self.assertEqual(result, mock_response)

    @patch('requests.get')
    def test_get_stadiums(self, mock_get):
        """
        Tests the get_stadiums method to ensure it correctly fetches team data from the API.

        Mocks the requests.get call to simulate an API response and verifies that the
        get_stadiums method returns the expected JSON data without making an actual API call.

        :param mock_get:
            A mock object that simulates the requests.get method.
        """
        mock_response = {'stadiums': []}

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response

        extract = Extract()
        result = extract.get_stadiums()

        self.assertEqual(result, mock_response)

    @patch('requests.get')
    def test_get_players(self, mock_get):
        """
        Tests the get_players method to ensure it correctly fetches team data from the API.

        Mocks the requests.get call to simulate an API response and verifies that the
        get_players method returns the expected data without making an actual API call.

        :param mock_get:
            A mock object that simulates the requests.get method.
        """
        mock_response = {'players': []}

        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response

        extract = Extract()
        result = extract.get_players()

        self.assertEqual(result, mock_response)

    def test_get_list_of_teams(self):
        """
        Tests get_list_of_teams function to ensure its correctly fetch teams from json file.

        Check the result that we want with what function returns.

        """
        response = ["WAS", "CHA", "ATL", "MIA", "ORL", "NY", "PHI", "BKN", "BOS", "TOR",
                    "CHI", "CLE", "IND", "DET", "MIL", "MIN", "UTA", "OKC", "POR", "DEN",
                    "MEM", "HOU", "NO", "SA", "DAL", "GS", "LAL", "LAC", "PHO", "SAC"]
        extract = Extract()
        result = extract.get_list_of_teams()
        self.assertEqual(response, result)
