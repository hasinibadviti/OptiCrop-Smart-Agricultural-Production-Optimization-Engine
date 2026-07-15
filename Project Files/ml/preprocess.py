"""
ml/preprocess.py
Handles data loading, cleaning, and preprocessing for the OptiCrop dataset.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from config import Config


def load_dataset():
    """
    Load the raw crop recommendation dataset from disk.

    Returns:
        pd.DataFrame: Raw dataset.
    """
    return pd.read_csv(Config.RAW_DATASET_PATH)


def clean_dataset(df):
    """
    Handle missing values and remove duplicate records.

    Args:
        df (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df


def save_processed_dataset(df):
    """
    Save the cleaned dataset to the processed data path.

    Args:
        df (pd.DataFrame): Cleaned dataset.
    """
    Config.PROCESSED_DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(Config.PROCESSED_DATASET_PATH, index=False)


def split_features_target(df):
    """
    Split the dataset into features and target.

    Args:
        df (pd.DataFrame): Cleaned dataset.

    Returns:
        tuple: (X, y) feature DataFrame and target Series.
    """
    X = df[Config.FEATURE_COLUMNS]
    y = df[Config.TARGET_COLUMN]
    return X, y


def scale_features(X_train, X_test):
    """
    Fit a StandardScaler on training features and transform both sets.

    Args:
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.

    Returns:
        tuple: (X_train_scaled, X_test_scaled, scaler)
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def split_train_test(X, y):
    """
    Split features and target into training and testing sets.

    Args:
        X (pd.DataFrame): Features.
        y (pd.Series): Target labels.

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    return train_test_split(
        X,
        y,
        test_size=Config.TEST_SIZE,
        random_state=Config.RANDOM_STATE,
        stratify=y,
    )


def preprocess_pipeline():
    """
    Run the full preprocessing pipeline: load, clean, save, split, scale.

    Returns:
        tuple: (X_train_scaled, X_test_scaled, y_train, y_test, scaler)
    """
    df = load_dataset()
    df = clean_dataset(df)
    save_processed_dataset(df)

    X, y = split_features_target(df)
    X_train, X_test, y_train, y_test = split_train_test(X, y)
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler