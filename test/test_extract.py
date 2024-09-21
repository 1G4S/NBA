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

        extract = Extract()
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
