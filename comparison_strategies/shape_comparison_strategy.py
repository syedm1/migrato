from comparison_strategies.comparison_strategy import ComparisonStrategy

class ShapeComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        old_data = self.get_value_with_depth(old_data, self.start_depth_old)
        new_data = self.get_value_with_depth(new_data, self.start_depth_new)
        return set(old_data.keys()) == set(new_data.keys())