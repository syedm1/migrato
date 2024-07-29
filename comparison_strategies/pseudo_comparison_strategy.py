from comparison_strategies.comparison_strategy import ComparisonStrategy

class PseudoComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        old_data = self.get_value_with_depth(old_data, self.start_depth_old)
        new_data = self.get_value_with_depth(new_data, self.start_depth_new)
        matched_keys = {}
        failed_keys = {}
        try:
            for key, old_value in old_data.items():
                new_value = new_data.get(key)
                if new_value == old_value:
                    matched_keys[key] = old_value
                else:
                    failed_keys[key] = {"old_value": old_value, "new_value": new_value}
            return matched_keys, failed_keys

        except AttributeError:
            return old_data == new_data