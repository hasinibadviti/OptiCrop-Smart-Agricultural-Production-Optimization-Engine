"""
app.py
Main entry point for the OptiCrop Flask application.
Initializes the Flask app, loads configuration, and registers blueprints.
"""

from flask import Flask
from config import DevelopmentConfig
from routes.main_routes import main_bp


def create_app(config_class=DevelopmentConfig):
    """
    Application factory function.
    Creates and configures the Flask application instance.
    """
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    # Load configuration
    app.config.from_object(config_class)

    # Register Blueprints,connects all routes to the application
    app.register_blueprint(main_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", True))