from comparison_strategy import ComparisonStrategy


class PseudoComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        matched_keys = {}
        failed_keys = {}
        for key in old_data.keys() | new_data.keys():
            old_value = old_data.get(key, None)
            new_value = new_data.get(key, None)
            if old_value == new_value:
                matched_keys[key] = old_value
            else:
                failed_keys[key] = {"old_value": old_value, "new_value": new_value}
        return matched_keys, failed_keys
