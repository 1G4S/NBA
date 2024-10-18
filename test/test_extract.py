import pytest
from extract.extract import Extract
from extract.strategies.players_retrieval_strategy import PlayersRetrievalStrategy
from extract.strategies.stadiums_retrieval_strategy import StadiumsRetrievalStrategy
from extract.strategies.teams_retrieval_strategy import TeamsRetrievalStrategy


def test_get_teams(mocker):
    """
    Tests the get_teams method to ensure it correctly fetches team data from the API.

    Mocks the requests.get call to simulate an API response and verifies that the
    get_teams method returns the expected JSON data without making an actual API call.
    """
    mock_response = {'teams': []}

    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    teams_strategy = TeamsRetrievalStrategy()
    extract = Extract(teams_strategy)
    result = extract.retrieve_specific_data()

    assert result == mock_response


def test_get_stadiums(mocker):
    """
    Tests the get_stadiums method to ensure it correctly fetches team data from the API.

    Mocks the requests.get call to simulate an API response and verifies that the
    get_stadiums method returns the expected JSON data without making an actual API call.
    """
    mock_response = {'stadiums': []}

    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    stadiums_strategy = StadiumsRetrievalStrategy()
    extract = Extract(stadiums_strategy)

    result = extract.retrieve_specific_data()

    assert result == mock_response


def test_get_players(mocker):
    """
    Tests the get_players method to ensure it correctly fetches team data from the API.

    Mocks the requests.get call to simulate an API response and verifies that the
    get_players method returns the expected data without making an actual API call.
    """
    mock_response = {'players': []}

    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    players_strategy = PlayersRetrievalStrategy()
    extract = Extract(players_strategy)

    result = extract.retrieve_specific_data()

    assert result is not None
    assert len(result) > 0


def test_get_list_of_teams():
    """
    Tests get_list_of_teams function to ensure it correctly fetches teams from a JSON file.

    Checks if the result from the function matches the expected list of teams.
    """
    response = ["WAS", "CHA", "ATL", "MIA", "ORL", "NY", "PHI", "BKN", "BOS", "TOR",
                "CHI", "CLE", "IND", "DET", "MIL", "MIN", "UTA", "OKC", "POR", "DEN",
                "MEM", "HOU", "NO", "SA", "DAL", "GS", "LAL", "LAC", "PHO", "SAC"]

    players_strategy = PlayersRetrievalStrategy()
    result = players_strategy.get_list_of_teams()

    assert result == response
