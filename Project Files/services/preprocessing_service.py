"""
services/preprocessing_service.py
Reusable helper functions for converting and validating numeric input
before passing data to the prediction service.
"""

from typing import Dict, Optional, Tuple

from utils.validation import validate_fields
from utils.helper import safe_float_conversion


def prepare_input_data(
    raw_data: Dict[str, Optional[str]]
) -> Tuple[bool, str, Dict[str, float]]:
    """
    Validate and convert raw form input into clean numeric data.

    Args:
        raw_data (Dict[str, Optional[str]]): Raw form field values.

    Returns:
        Tuple[bool, str, Dict[str, float]]: A tuple of
            (is_valid, error_message, cleaned_data).
    """
    is_valid, error_message = validate_fields(raw_data)

    if not is_valid:
        return False, error_message, {}

    cleaned_data: Dict[str, float] = {}
    for field, value in raw_data.items():
        converted_value = safe_float_conversion(value)
        if converted_value is None:
            return False, f"Invalid numeric value for field: {field}", {}
        cleaned_data[field] = converted_value

    return True, "", cleaned_data