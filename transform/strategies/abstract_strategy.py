from abc import ABC, abstractmethod

from extract.extract import Extract


class Strategy(ABC):

    @abstractmethod
    def get_data(self, extract: Extract):
        """
        Abstract method to retrieve and transform data using an Extract instance.

        Parameters
        ----------
        extract : Extract
            An instance of the `Extract` class used to retrieve raw data.
        """
        pass
