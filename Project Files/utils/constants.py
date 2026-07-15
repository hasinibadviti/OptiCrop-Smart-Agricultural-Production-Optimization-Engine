"""
utils/constants.py
Stores application-wide constants used across the OptiCrop project.
"""

APP_TITLE: str = "OptiCrop - Smart Agricultural Production Optimization Engine"

FIELD_NAMES = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall",
]

# Valid input ranges: (min_value, max_value)
FIELD_RANGES = {
    "N": (0, 140),
    "P": (0, 145),
    "K": (0, 205),
    "temperature": (-10, 60),
    "humidity": (0, 100),
    "ph": (0, 14),
    "rainfall": (0, 400),
}

MESSAGES = {
    "empty_field": "All input fields are required. Please fill in every field.",
    "invalid_number": "All input values must be valid numbers.",
    "out_of_range": "One or more input values are out of the accepted range.",
    "prediction_success": "Prediction generated successfully.",
    "prediction_error": "Failed to generate prediction. Please try again.",
}