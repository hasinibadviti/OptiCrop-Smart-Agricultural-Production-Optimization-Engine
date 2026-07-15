"""
config.py
Centralized configuration for OptiCrop application.
Defines paths, Flask settings, and reusable constants.
"""

from pathlib import Path


class Config:
    # ---------------- Base Directory ----------------
    BASE_DIR = Path(__file__).resolve().parent

    # ---------------- Dataset Paths ----------------
    DATASET_DIR = BASE_DIR / "dataset"
    RAW_DATASET_PATH = DATASET_DIR / "Crop_recommendation.csv"
    PROCESSED_DATASET_PATH = DATASET_DIR / "processed_data.csv"

    # ---------------- ML Model Paths ----------------
    ML_DIR = BASE_DIR / "ml"
    MODEL_PATH = ML_DIR / "model.pkl"
    SCALER_PATH = ML_DIR / "scaler.pkl"

    # ---------------- Reports Paths ----------------
    REPORTS_DIR = BASE_DIR / "reports"
    MODEL_METRICS_PATH = REPORTS_DIR / "model_metrics.txt"
    CONFUSION_MATRIX_PATH = REPORTS_DIR / "confusion_matrix.png"

    # ---------------- Static & Templates ----------------
    STATIC_DIR = BASE_DIR / "static"
    TEMPLATES_DIR = BASE_DIR / "templates"

    # ---------------- Flask Settings ----------------
    SECRET_KEY = "opticrop-secret-key-2024"
    DEBUG = True
    TESTING = False
    JSON_SORT_KEYS = False

    # ---------------- Model Features ----------------
    FEATURE_COLUMNS = [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall",
    ]

    TARGET_COLUMN = "label"

    # ---------------- Train/Test Split ----------------
    TEST_SIZE = 0.2
    RANDOM_STATE = 42


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}