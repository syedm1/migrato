class ComparisonStrategy:
    def compare(self, old_data, new_data):
        raise NotImplementedError("This method should be overridden by subclasses")

class ExactComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        return old_data == new_data

class ShapeComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        return isinstance(old_data, type(new_data)) and len(old_data) == len(new_data)

class CustomComparisonStrategy(ComparisonStrategy):
    def __init__(self, custom_mapping):
        self.custom_mapping = custom_mapping

    def compare(self, old_data, new_data):
        old_transformed = {self.custom_mapping.get(k, k): v for k, v in old_data.items()}
        return old_transformed == new_data

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

class OrderingCheckComparisonStrategy(ComparisonStrategy):
    def compare(self, old_data, new_data):
        return old_data == new_data

def get_nested_value(data, keys):
    for key in keys.split('.'):
        data = data[key]
    return data

class ComparisonStrategyFactory:
    @staticmethod
    def get_comparison_strategy(comparison):
        comparison_type = comparison.get('comparison_type')
        if comparison_type == 'exact':
            return ExactComparisonStrategy()
        elif comparison_type == 'shape':
            return ShapeComparisonStrategy()
        elif comparison_type == 'custom':
            custom_mapping = comparison.get('custom_mapping', {})
            return CustomComparisonStrategy(custom_mapping)
        elif comparison_type == 'specific':
            specific_match = comparison.get('specific_match', {})
            return SpecificComparisonStrategy(specific_match)
        elif comparison_type == 'pseudo':
            return PseudoComparisonStrategy()
        elif comparison_type == 'orderingCheck':
            return OrderingCheckComparisonStrategy()
        else:
            raise ValueError(f"Unknown comparison type: {comparison_type}")
