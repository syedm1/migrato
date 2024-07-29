from comparison_strategies.custom_comparison_strategy import CustomComparisonStrategy
from comparison_strategies.exact_comparison_strategy import ExactComparisonStrategy
from comparison_strategies.pseudo_comparison_strategy import PseudoComparisonStrategy
from comparison_strategies.shape_comparison_strategy import ShapeComparisonStrategy
from comparison_strategies.specific_comparison_strategy import SpecificComparisonStrategy


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
        else:
            raise ValueError(f"Unknown comparison type: {comparison_type}")
