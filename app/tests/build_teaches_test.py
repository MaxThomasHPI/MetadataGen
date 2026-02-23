from app.metadatabuilder.deprecated.build_teaches import build_all_teaches
from pprint import pprint


test_input = [
    {
        "educationalFramework": "ESCO",
        "conceptUrl": "http://data.europa.eu/esco/skill/5bdb8e03-04ab-4869-a48f-3b013b5a2c3c"
    }
]

pprint(build_all_teaches(test_input))
