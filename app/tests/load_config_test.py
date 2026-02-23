from app.helper.load_config import load_framework_conf, load_suggestion_engine_conf
from pprint import pprint

framework = "DigComp"
group = "educationalLevel"


data = load_framework_conf(framework, group)

pprint(type(data["ID"]))

pprint(load_suggestion_engine_conf())
