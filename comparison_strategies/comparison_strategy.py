from abc import ABC, abstractmethod
from utils import get_nested_value

class ComparisonStrategy(ABC):
    def __init__(self, comparison):
        self.start_depth_old = comparison.get('start_depth_old', '')
        self.start_depth_new = comparison.get('start_depth_new', '')

    def get_value_with_depth(self, data, depth):
        if depth:
            return get_nested_value(data, depth)
        return data

    @abstractmethod
    def compare(self, old_data, new_data):
        pass