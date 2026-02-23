from app.metadatabuilder.deprecated.build_educational_level import build_educational_level
from pprint import pprint

test_input = {
    "educationalFramework": "DigComp",
    "conceptUrl": "https://metadata-generator.xikolo.de/framework/digcomp/5"
}

pprint(build_educational_level(test_input))
