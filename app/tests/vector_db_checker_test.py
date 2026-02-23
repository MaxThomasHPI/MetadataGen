from app.suggestion_engine.vector_dbs_checker import check_for_vector_dbs
from app.helper.paths import APP_ROOT
from app.helper.load_config import load_suggestion_engine_conf

path = (
    APP_ROOT /
    "suggestion_engine" /
    "conf.yml"
)

conf = load_suggestion_engine_conf()

print(check_for_vector_dbs(conf))
