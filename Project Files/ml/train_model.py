"""
ml/train_model.py
Trains multiple ML classification models, compares their performance,
and persists the best performing model along with the fitted scaler.
"""

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from config import Config
from ml.preprocess import preprocess_pipeline
from ml.evaluate import evaluate_model, save_metrics_report, save_confusion_matrix


def get_candidate_models():
    """
    Define the candidate models to train and compare.

    Returns:
        dict: Mapping of model name to an untrained model instance.
    """
    return {
        "Logistic Regression": LogisticRegression(
            max_iter=1000, random_state=Config.RANDOM_STATE
        ),
        "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
        "Decision Tree Classifier": DecisionTreeClassifier(
            random_state=Config.RANDOM_STATE
        ),
        "Random Forest Classifier": RandomForestClassifier(
            n_estimators=200, random_state=Config.RANDOM_STATE
        ),
    }


def train_and_compare_models(X_train, X_test, y_train, y_test):
    """
    Train all candidate models and compare their test accuracy.

    Args:
        X_train, X_test, y_train, y_test: Train/test splits.

    Returns:
        tuple: (results dict, best_model_name, best_model, best_predictions)
    """
    models = get_candidate_models()
    results = {}
    trained_models = {}
    predictions = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        results[name] = acc
        trained_models[name] = model
        predictions[name] = y_pred

    best_model_name = max(results, key=results.get)
    best_model = trained_models[best_model_name]
    best_predictions = predictions[best_model_name]

    return results, best_model_name, best_model, best_predictions


def save_model_artifacts(model, scaler):
    """
    Save the trained model and fitted scaler using joblib.

    Args:
        model: Trained best-performing model.
        scaler: Fitted StandardScaler instance.
    """
    Config.MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, Config.MODEL_PATH)
    joblib.dump(scaler, Config.SCALER_PATH)


def run_training_pipeline():
    """
    Execute the complete training pipeline:
    preprocessing, training, comparison, evaluation, and persistence.
    """
    X_train, X_test, y_train, y_test, scaler = preprocess_pipeline()

    results, best_model_name, best_model, best_predictions = train_and_compare_models(
        X_train, X_test, y_train, y_test
    )

    save_model_artifacts(best_model, scaler)

    metrics = evaluate_model(y_test, best_predictions)
    save_metrics_report(results, best_model_name, metrics)
    save_confusion_matrix(y_test, best_predictions, best_model.classes_)

    print("Model comparison results:")
    for name, acc in results.items():
        print(f"  {name}: {acc:.4f}")
    print(f"\nBest Model Selected: {best_model_name}")
    print(f"Model saved to: {Config.MODEL_PATH}")
    print(f"Scaler saved to: {Config.SCALER_PATH}")


if __name__ == "__main__":
    run_training_pipeline()