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
            return ExactComparisonStrategy(comparison)
        elif comparison_type == 'shape':
            return ShapeComparisonStrategy(comparison)
        elif comparison_type == 'custom':
            return CustomComparisonStrategy(comparison)
        elif comparison_type == 'specific':
            return SpecificComparisonStrategy(comparison)
        elif comparison_type == 'pseudo':
            return PseudoComparisonStrategy(comparison)
        else:
            raise ValueError(f"Unknown comparison type: {comparison_type}")