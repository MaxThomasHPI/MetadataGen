import json


def extract_narrower_concepts(entry):
    return json.loads(entry["narrowerconcept"].replace("'", '"'))


def prepare_entry(entry):
    return {
        "name": entry["name"],
        "uri": entry["uri"],
        "hasNarrower": len(extract_narrower_concepts(entry)) > 0
    }
