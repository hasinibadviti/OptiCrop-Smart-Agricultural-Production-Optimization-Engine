"""
utils/validation.py
Validation utilities for verifying user input before prediction.
"""

from typing import Dict, Optional, Tuple

from utils.constants import FIELD_NAMES, FIELD_RANGES, MESSAGES
from utils.helper import is_blank, safe_float_conversion


def validate_fields(raw_data: Dict[str, Optional[str]]) -> Tuple[bool, str]:
    """
    Validate raw input fields for presence, numeric type, and valid range.

    Args:
        raw_data (Dict[str, Optional[str]]): Raw form field values.

    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    for field in FIELD_NAMES:
        value = raw_data.get(field)

        if is_blank(value):
            return False, MESSAGES["empty_field"]

        numeric_value = safe_float_conversion(value)
        if numeric_value is None:
            return False, MESSAGES["invalid_number"]

        min_value, max_value = FIELD_RANGES[field]
        if not (min_value <= numeric_value <= max_value):
            return False, MESSAGES["out_of_range"]

    return True, ""