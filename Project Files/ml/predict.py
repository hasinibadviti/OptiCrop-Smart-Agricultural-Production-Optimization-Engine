"""
ml/predict.py
Loads the trained model and scaler to perform crop predictions
based on soil and environmental input parameters.
"""

import joblib
import pandas as pd

from config import Config

_model = None
_scaler = None


def load_artifacts():
    """
    Load the trained model and fitted scaler from disk using joblib.
    Caches artifacts in memory after first load.

    Returns:
        tuple: (model, scaler)
    """
    global _model, _scaler

    if _model is None:
        _model = joblib.load(Config.MODEL_PATH)

    if _scaler is None:
        _scaler = joblib.load(Config.SCALER_PATH)

    return _model, _scaler


def predict_crop(n, p, k, temperature, humidity, ph, rainfall):
    """
    Predict the most suitable crop based on the provided input parameters.

    Args:
        n (float): Nitrogen content.
        p (float): Phosphorous content.
        k (float): Potassium content.
        temperature (float): Temperature in Celsius.
        humidity (float): Relative humidity percentage.
        ph (float): Soil pH value.
        rainfall (float): Rainfall in mm.

    Returns:
        str: Predicted crop label.
    """
    model, scaler = load_artifacts()

    input_df = pd.DataFrame(
        [[n, p, k, temperature, humidity, ph, rainfall]],
        columns=Config.FEATURE_COLUMNS,
    )

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)

    return str(prediction[0])