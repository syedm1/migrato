from enum import Enum


class ComparisonType(Enum):
    EXACT = "exact"
    SHAPE = "shape"
    CUSTOM = "custom"
    PSEUDO = "pseudo"
    SPECIFIC = "specific"
    ORDERING_CHECK = "orderingCheck"

    @staticmethod
    def is_valid_enum(comparison_type: str) -> bool:
        return comparison_type in ComparisonType._value2member_map_

    @staticmethod
    def get_enum_from_string(comparison_type: str) -> 'ComparisonType':
        if ComparisonType.is_valid_enum(comparison_type):
            return ComparisonType(comparison_type)
        else:
            raise ValueError(f"Invalid comparison type: {comparison_type}")

    @staticmethod
    def get_string_from_enum(comparison_type: 'ComparisonType') -> str:
        return comparison_type.value