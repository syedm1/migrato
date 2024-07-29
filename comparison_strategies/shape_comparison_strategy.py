from comparison_strategy import ComparisonStrategy

class ShapeComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        return isinstance(old_data, type(new_data)) and len(old_data) == len(new_data)
