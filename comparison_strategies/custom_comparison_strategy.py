from comparison_strategies.comparison_strategy import ComparisonStrategy


class CustomComparisonStrategy(ComparisonStrategy):
    def __init__(self, custom_mapping):
        self.custom_mapping = custom_mapping

    def compare(self, old_data, new_data):
        old_transformed = {self.custom_mapping.get(k, k): v for k, v in old_data.items()}
        return old_transformed == new_data
