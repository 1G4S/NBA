import pytest
import pandas as pd
from unittest.mock import Mock
from extract.extract import Extract
from transform.strategies.abstract_strategy import Strategy
from transform.strategies.players_strategy import PlayersStrategy
from transform.transform import Transform


def test_transform_initialization():
    """
    Tests the initialization of the Transform class by verifying that
    the given strategy and extract parameters are correctly assigned to
    the transform instance.

    :return: None
    """
    mock_strategy = Mock(spec=Strategy)
    mock_extract = Mock(spec=Extract)

    transform = Transform(mock_strategy, mock_extract)
    assert transform.strategy == mock_strategy
    assert transform.extract == mock_extract


def test_transform_getter_strategy():
    """
    Unit test for the Transform class to verify the getter method for the strategy attribute.

    :return: None
    """
    mock_strategy = Mock(spec=Strategy)
    mock_extract = Mock(spec=Extract)

    transform = Transform(mock_strategy, mock_extract)
    assert transform.strategy == mock_strategy


def test_transform_setter_strategy():
    """
    Tests the setter method for the strategy attribute in the Transform class.

    This test checks whether the strategy attribute of an instance of the
    Transform class can be successfully updated to a new strategy.

    It uses the Mock library to create mock objects for the Strategy,
    Extract, and PlayersStrategy classes. A Transform object is instantiated
    with the mock strategy and extract objects. The strategy attribute is then
    set to a new mock strategy. The test asserts that the strategy has been
    successfully updated.

    :return: None
    """
    mock_strategy = Mock(spec=Strategy)
    mock_extract = Mock(spec=Extract)
    mock_new_strategy = Mock(spec=PlayersStrategy)

    transform = Transform(mock_strategy, mock_extract)
    transform.strategy = mock_new_strategy

    assert transform.strategy == mock_new_strategy


def test_delete_columns():
    """
    Tests the delete_columns function of the Transform class.

    This test verifies that the delete_columns function correctly removes the specified columns from
    the input DataFrame.

    :return: None
    """
    before_deletion = pd.DataFrame({
        'c1': [1, 2, 3],
        'c2': [4, 5, 6],
        'c3': [7, 8, 9]
    })

    after_deletion = pd.DataFrame({
        'c2': [4, 5, 6]
    })
    mock_strategy = Mock(spec=PlayersStrategy)
    mock_strategy.list_of_columns_to_remove = ['c1', 'c3']
    mock_extract = Mock(spec=Extract)

    transform = Transform(mock_strategy, mock_extract)
    result = transform.delete_columns(before_deletion)

    assert result.equals(after_deletion)


def test_normalize_to_pandas():
    """
    Tests the normalize_to_pandas function of the Transform class.

    This test verifies that the normalize_to_pandas function correctly turn mock_data into a DataFrame.

    :return: None
    """
    mock_data = {
        'c1': [1, 2, 3],
        'c2': [4, 5, 6],
        'c3': [7, 8, 9]
    }
    mock_extract = Mock(spec=Extract)
    mock_extract.retrieve_specific_data.return_value = mock_data

    players_strategy = PlayersStrategy()
    transform = Transform(players_strategy, mock_extract)
    result = transform.normalize_to_pandas()
    assert isinstance(result, pd.DataFrame)


def test_get_clean_data():
    """
    Function to test the `get_clean_data` method of the `Transform` class.

    :return: Assertion if the actual result matches the expected dataframe after deletion of specified columns.
    """
    before_deletion = {
        'c1': [1, 2, 3],
        'c2': [4, 5, 6],
        'c3': [7, 8, 9]
    }
    after_deletion = pd.DataFrame({
        'c2': [4, 5, 6]
    })

    mock_strategy = Mock(spec=PlayersStrategy)
    mock_strategy.list_of_columns_to_remove = ['c1', 'c3']
    mock_strategy.get_data.return_value = before_deletion
    mock_extract = Mock(spec=Extract)

    transform = Transform(mock_strategy, mock_extract)
    result = transform.get_clean_data()

    assert result.equals(after_deletion)
