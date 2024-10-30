import pytest
import pandas as pd
from unittest.mock import Mock
from extract.extract import Extract
from transform.strategies.abstract_transform_strategy import TransformStrategy
from transform.strategies.players_transform_strategy import PlayersTransformStrategy
from transform.transform import Transform


def test_transform_initialization():
    """
    Tests the initialization of the Transform class with a mock strategy.

    This test:
    - Creates a mock object for the PlayersTransformStrategy.
    - Initializes the Transform class with the mock strategy.
    - Asserts that the strategy attribute of the transform instance is correctly set to the mock strategy.

    :return: None
    """
    mock_strategy = Mock(spec=PlayersTransformStrategy)

    transform = Transform(mock_strategy)
    assert transform.strategy == mock_strategy


def test_transform_getter_strategy():
    """
    Tests the behavior of the Transform class's getter for the strategy attribute.

    :return: None
    """
    mock_strategy = Mock(spec=PlayersTransformStrategy)

    transform = Transform(mock_strategy)
    assert transform.strategy == mock_strategy


def test_transform_setter_strategy():
    """
    Tests the setter method for the strategy used in the Transform class.

    This function creates mock objects for both the initial and new strategy.
    It verifies that the new strategy is correctly set and retrieved.

    :return: None
    """
    mock_strategy = Mock(spec=TransformStrategy)
    mock_new_strategy = Mock(spec=PlayersTransformStrategy)

    transform = Transform(mock_strategy)
    transform.strategy = mock_new_strategy

    assert transform.strategy == mock_new_strategy


def test_delete_columns():
    """
    Tests the deletion of specified columns from a DataFrame using a mock strategy.

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
    mock_strategy = Mock(spec=PlayersTransformStrategy)
    mock_strategy.list_of_columns_to_remove = ['c1', 'c3']

    transform = Transform(mock_strategy)
    result = transform.delete_columns(before_deletion)

    assert result.equals(after_deletion)


def test_normalize_to_pandas():
    """
    Tests the `normalize_to_pandas` method of the `Transform` class using mock data.
    The test checks if the returned result from the method is an instance of `pd.DataFrame`.

    :return: None
    """
    mock_data = {
        'c1': [1, 2, 3],
        'c2': [4, 5, 6],
        'c3': [7, 8, 9]
    }

    players_strategy = PlayersTransformStrategy(mock_data)
    transform = Transform(players_strategy)
    result = transform.normalize_to_pandas()
    assert isinstance(result, pd.DataFrame)


def test_get_clean_data():
    """
    Tests the `get_clean_data` method of the `Transform` class to ensure that it correctly removes specified columns from the input data.

    :return: None
    """
    before_deletion = {
        'c1': [1, 2, 3],
        'c2': [4, 5, 6],
        'c3': [7, 8, 9]
    }
    after_deletion = pd.DataFrame({
        'c2': [4, 5, 6]
    })
    players_transform_strategy = PlayersTransformStrategy(before_deletion)
    players_transform_strategy.list_of_columns_to_remove = ['c1', 'c3']
    transform = Transform(players_transform_strategy)
    result = transform.get_clean_data()

    assert result.equals(after_deletion)
