from abc import ABC, abstractmethod


class ExtractStrategy(ABC):
    @abstractmethod
    def retrieve_data(self):
        pass
