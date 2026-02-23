from app.metadatabuilder.build_framework_metadata import build_all_framework_metadata


def build_optional_metadata(data: dict) -> dict:
    """
    Creates a dictionary with the optional metadata. Provided data will be checked for
    eligible metadata attributes.

    :param data: The input metadata to be enriched and restructured to fit the MOOChub format
    :type data: dict
    :return: A metadata dictionary containing optional attributes conforming to the MOOChub
    metadata structure.
    :rtype: dict
    """
    optional_attributes = {  # expendable to fit further optional attributes
        "startDate": lambda date: [date],
        "endDate": lambda date: [date],
        "keywords": lambda keywords: keywords,
    }

    optional_metadata = dict()

    for optional_attribute, fragment_function in optional_attributes.items():
        if optional_attribute in data.keys():
            optional_metadata[optional_attribute] = fragment_function(data[optional_attribute])

    groups = [
        "educationalAlignment",
        "teaches",
        "educationalLevel"
    ]

    for group in groups:
        if group in data.keys():
            optional_metadata[group] = build_all_framework_metadata(data[group], group)

    return optional_metadata
