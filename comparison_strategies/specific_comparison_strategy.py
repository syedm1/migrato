from comparison_strategies.comparison_strategy import ComparisonStrategy

class SpecificComparisonStrategy(ComparisonStrategy):
    def __init__(self, comparison):
        super().__init__(comparison)
        self.specific_match = comparison.get('specific_match', {})

    def compare(self, old_data, new_data):
        old_key = self.specific_match.get('old', '')
        new_key = self.specific_match.get('new', '')
        return old_data.get(old_key) == new_data.get(new_key)