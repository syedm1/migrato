from comparison_strategy import ComparisonStrategy

class ExactComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        return old_data == new_data
