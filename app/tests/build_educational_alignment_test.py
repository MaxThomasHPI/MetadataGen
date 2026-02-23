from app.metadatabuilder.deprecated.build_educational_alignment import build_all_educational_alignments
from pprint import pprint


test_input = [
    {
        "educationalFramework": "ISCED-F",
        "conceptUrl": "http://data.europa.eu/esco/isced-f/0831"
    }
]

pprint(build_all_educational_alignments(test_input))
