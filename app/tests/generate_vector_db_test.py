from app.helper.load_config import load_suggestion_engine_conf
from app.helper.paths import APP_ROOT
from app.suggestion_engine.vector_db_creator import create_vector_db

path_conf = (
    APP_ROOT /
    "suggestion_engine" /
    "conf.yml"
)
conf = load_suggestion_engine_conf()

create_vector_db("ISCED-F", conf)
