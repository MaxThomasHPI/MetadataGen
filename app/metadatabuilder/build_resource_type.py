def build_resource_type_fragment() -> dict:
    """
    Creates a predefined and mandatory "resourceType" fragment.

    :return: A predefined "resourceType" fragment.
    :rtype: dict
    """
    resource_type = {
        "identifier": "https://w3id.org/kim/hcrt/course",
        "type": "Concept",
        "inScheme": "https://w3id.org/kim/hcrt/scheme"
    }

    return resource_type
