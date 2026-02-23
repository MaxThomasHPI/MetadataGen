def generate_name_and_description_fragment(additional_data, conf):
    """
    Generates a data fragment with a name and a description according to the MOOChub
    specification.

    :param additional_data: The basic data to be enriched and converted into the specified format.
    :type additional_data: dict
    :param conf: The config file related to the data.
    :type conf: dict
    :return: The data fragment for name and description according to the MOOChub specification.
    :rtype: dict
    """
    name = [{
        "name": additional_data["name"],
        "inLanguage": conf["LANGUAGE"]
    }]

    if "description" in additional_data.keys() and additional_data["description"] not in [None, ""] \
            and type(additional_data["description"]) != float:
        return {
            "name": name,
            "description": additional_data["description"]
        }
    return {"name": name}
