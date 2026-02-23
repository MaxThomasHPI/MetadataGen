from app.suggestion_engine import vector_dbs_checker, vector_db_creator
from app.helper.load_config import load_suggestion_engine_conf
from app.helper.paths import SUGGESTION_ENGINE_CONF
from flask import Flask


def create_app() -> Flask:
    """
    Checks for missing vector databases and creates them if necessary. Subsequently,
    creates the Flask application object and registers the routes.

    :return: The Flask application.
    :rtype: Flask
    """
    print("Start program ...")
    setup_vector_databases()

    print("Create Flask object ...")
    app = Flask(__name__, static_folder='static')

    print("Register routes ...")
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    print("Setup complete ...")
    print("Start server ...")
    return app


def setup_vector_databases():
    print("Setup vector data bases ...")
    conf = load_suggestion_engine_conf()

    print("Searching for existing and missing vector databases ...")
    missing_frameworks, framework_conf = vector_dbs_checker.check_for_vector_dbs(conf)
    print(f"Found {len(missing_frameworks)} missing data bases ...")

    for framework in missing_frameworks:
        vector_db_creator.create_vector_db(framework, framework_conf)