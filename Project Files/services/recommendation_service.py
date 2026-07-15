"""
services/recommendation_service.py
Business logic layer for generating crop recommendations.
"""

from typing import Dict

from ml.predict import predict_crop


def get_crop_recommendation(input_data: Dict[str, float]) -> str:
    """
    Generate a crop recommendation using the trained ML model.

    Args:
        input_data (Dict[str, float]): Validated numeric input parameters
            containing N, P, K, temperature, humidity, ph, and rainfall.

    Returns:
        str: Predicted crop label.
    """
    predicted_crop = predict_crop(
        n=input_data["N"],
        p=input_data["P"],
        k=input_data["K"],
        temperature=input_data["temperature"],
        humidity=input_data["humidity"],
        ph=input_data["ph"],
        rainfall=input_data["rainfall"],
    )
    return predicted_crop