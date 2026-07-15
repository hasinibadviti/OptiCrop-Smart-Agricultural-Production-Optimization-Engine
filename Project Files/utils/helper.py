"""
utils/helper.py
General-purpose helper utilities used across the OptiCrop application.
"""

from typing import Optional


def safe_float_conversion(value: Optional[str]) -> Optional[float]:
    """
    Safely convert a string value to a float.

    Args:
        value (Optional[str]): The value to convert.

    Returns:
        Optional[float]: The converted float value, or None if conversion fails.
    """
    if value is None:
        return None

    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def is_blank(value: Optional[str]) -> bool:
    """
    Check whether a given value is None or an empty/whitespace-only string.

    Args:
        value (Optional[str]): The value to check.

    Returns:
        bool: True if the value is blank, False otherwise.
    """
    return value is None or str(value).strip() == ""