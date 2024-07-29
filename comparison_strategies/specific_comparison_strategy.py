from comparison_strategies.comparison_strategy import ComparisonStrategy
from utils import get_nested_value


class SpecificComparisonStrategy(ComparisonStrategy):
    def __init__(self, specific_match):
        self.specific_match = specific_match

    def compare(self, old_data, new_data):
        try:
            old_value = get_nested_value(old_data, self.specific_match['old'])
            new_value = get_nested_value(new_data, self.specific_match['new'])
            return old_value == new_value
        except KeyError:
            return False
