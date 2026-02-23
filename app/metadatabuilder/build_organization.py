def build_organization_fragment(org_data: dict) -> dict:
    """
    Adds the mandatory "type" attribute to the organization metadata fragment and sets it to "Organization".

    :param org_data: A raw Organization object.
    :type org_data: dict
    :return: A Organization object with the minimal requirements to conform with the MOOChub format.
    :rtype: dict
    """
    org_data["type"] = "Organization"

    return org_data
