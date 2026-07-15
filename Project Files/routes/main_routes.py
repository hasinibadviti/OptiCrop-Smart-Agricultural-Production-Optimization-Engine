"""
routes/main_routes.py
Defines the main Flask Blueprint and view functions for OptiCrop.
"""

from flask import Blueprint, render_template, request

from services.recommendation_service import get_crop_recommendation
from services.preprocessing_service import prepare_input_data
from utils.constants import APP_TITLE, FIELD_NAMES

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    """
    Render the home page with the crop prediction input form.
    """
    return render_template("index.html", app_title=APP_TITLE)


@main_bp.route("/about", methods=["GET"])
def about():
    """
    Render the about page.
    """
    return render_template("about.html", app_title=APP_TITLE)


@main_bp.route("/predict", methods=["POST"])
def predict():
    """
    Handle prediction requests: validate form input, run prediction,
    and render the result page. Renders the error page on failure.
    """
    try:
        raw_data = {field: request.form.get(field) for field in FIELD_NAMES}

        is_valid, error_message, cleaned_data = prepare_input_data(raw_data)

        if not is_valid:
            return render_template(
                "error.html", app_title=APP_TITLE, error_message=error_message
            )

        predicted_crop = get_crop_recommendation(cleaned_data)

        return render_template(
            "result.html",
            app_title=APP_TITLE,
            predicted_crop=predicted_crop,
            input_data=cleaned_data,
        )

    except Exception as exc:
        return render_template(
            "error.html",
            app_title=APP_TITLE,
            error_message=f"An unexpected error occurred: {exc}",
        )