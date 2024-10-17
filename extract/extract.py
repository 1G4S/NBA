import json

import requests
from requests import RequestException

from extract.strategies.abstract_strategy import ExtractStrategy


class Extract:

    def __init__(self, strategy: ExtractStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> ExtractStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ExtractStrategy) -> None:
        self._strategy = strategy

    def retrieve_specific_data(self):
        return self._strategy.retrieve_data()
