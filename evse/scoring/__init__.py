"""
The :mod:`evse.scoring` module includes tools related to performances evaluation and scoring matrix creation
"""

from ._submission import YearlyResult, get_scoring_dataframe

__all__ = [
    "get_scoring_dataframe",
    "YearlyResult",
]
