from abc import ABC, abstractmethod


class ExtractStrategy(ABC):
    """
    Abstract base class that defines the interface for a data extraction strategy.

    This class enforces the implementation of a `retrieve_data` method, which
    should be overridden by subclasses to provide specific data retrieval logic.
    """

    @abstractmethod
    def retrieve_data(self):
        pass
