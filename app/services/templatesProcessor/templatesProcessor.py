templates = {
    "templateGeneral": [
        {"id": "name", "type": "tf", "mandatory": True, "test": False},
        {"id": "description", "type": "ta", "mandatory": True, "test": False},
        {"id": "url", "type": "tf", "mandatory": True, "test": "url"},
        {"id": "startDate", "type": "tf", "mandatory": False, "test": "date"},
        {"id": "endDate", "type": "tf", "mandatory": False, "test": "date"},
    ],
    "templateLicense": [
        {"id": "identifier", "type": "dd", "mandatory": True, "test": False}
    ],
    "templateOrganization": [
        {"id": "name", "type": "tf", "mandatory": True, "test": False},
        {"id": "url", "type": "tf", "mandatory": False, "test": "url"},
        {"id": "description", "type": "ta", "mandatory": False, "test": False}
    ],
    "templatePerson": [
        {"id": "name", "type": "tf", "mandatory": True, "test": False},
        {"id": "honorificPrefix", "type": "tf", "mandatory": False, "test": False},
        {"id": "description", "type": "ta", "mandatory": False, "test": False}
    ]
}


def gather_all_templates_data():
    return templates
