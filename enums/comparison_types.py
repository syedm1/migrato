from enum import Enum


class ComparisonType(Enum):
    EXACT = "exact"
    SHAPE = "shape"
    CUSTOM = "custom"
    PSEUDO = "pseudo"
    SPECIFIC = "specific"
    ORDERING_CHECK = "orderingCheck"

    
