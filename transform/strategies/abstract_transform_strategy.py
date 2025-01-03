from abc import ABC, abstractmethod

from extract.extract import Extract


class TransformStrategy(ABC):

    @abstractmethod
    def get_data(self):
        """
        Abstract method to retrieve and transform data using an Extract instance.
        """
        pass
