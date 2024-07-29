from abc import ABC, abstractmethod


class ComparisonStrategy(ABC):
    @abstractmethod
    def compare(self, old_data, new_data):
        pass