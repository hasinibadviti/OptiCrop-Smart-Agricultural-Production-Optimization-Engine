"""
ml/evaluate.py
Provides model evaluation utilities including metrics computation,
classification reports, and confusion matrix visualization.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from config import Config


def evaluate_model(y_test, y_pred):
    """
    Compute standard classification evaluation metrics.

    Args:
        y_test (array-like): True labels.
        y_pred (array-like): Predicted labels.

    Returns:
        dict: Computed metrics and classification report string.
    """
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
        "recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
        "f1_score": f1_score(y_test, y_pred, average="weighted", zero_division=0),
        "classification_report": classification_report(y_test, y_pred, zero_division=0),
    }
    return metrics


def save_metrics_report(results, best_model_name, metrics):
    """
    Save model comparison results and evaluation metrics to a text report.

    Args:
        results (dict): Mapping of model name to accuracy.
        best_model_name (str): Name of the selected best model.
        metrics (dict): Evaluation metrics of the best model.
    """
    Config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with open(Config.MODEL_METRICS_PATH, "w", encoding="utf-8") as f:
        f.write("OptiCrop - Model Evaluation Report\n")
        f.write("=" * 50 + "\n\n")

        f.write("Model Comparison (Accuracy):\n")
        f.write("-" * 50 + "\n")
        for name, acc in results.items():
            f.write(f"{name}: {acc:.4f}\n")

        f.write("\n")
        f.write(f"Best Model Selected: {best_model_name}\n")
        f.write("=" * 50 + "\n\n")

        f.write("Evaluation Metrics (Best Model):\n")
        f.write("-" * 50 + "\n")
        f.write(f"Accuracy  : {metrics['accuracy']:.4f}\n")
        f.write(f"Precision : {metrics['precision']:.4f}\n")
        f.write(f"Recall    : {metrics['recall']:.4f}\n")
        f.write(f"F1-Score  : {metrics['f1_score']:.4f}\n\n")

        f.write("Classification Report:\n")
        f.write("-" * 50 + "\n")
        f.write(metrics["classification_report"])
        f.write("\n")


def save_confusion_matrix(y_test, y_pred, class_labels):
    """
    Generate and save a confusion matrix heatmap image.

    Args:
        y_test (array-like): True labels.
        y_pred (array-like): Predicted labels.
        class_labels (array-like): Ordered class labels.
    """
    Config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    cm = confusion_matrix(y_test, y_pred, labels=class_labels)

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=class_labels,
        yticklabels=class_labels,
    )
    plt.title("Confusion Matrix - OptiCrop Best Model")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.tight_layout()

    plt.savefig(Config.CONFUSION_MATRIX_PATH)
    plt.close()