from abc import ABC, abstractmethod

from extract.extract import Extract


class Strategy(ABC):

    @abstractmethod
    def get_data(self, extract: Extract):
        pass
