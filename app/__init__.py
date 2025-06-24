"""Initializes the app and registers the endpoints"""


from flask import Flask


def create_app() -> Flask:
    """
    Creates the Flask application object and registers the routes.

    :return: The Flask application.
    :rtype: Flask
    """
    app = Flask(__name__, static_folder='static')

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
