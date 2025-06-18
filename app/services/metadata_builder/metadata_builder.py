"""
Builds the separate metadata fragments of the different attributes and combines
them to a complete MOOChub conform metadata file for a single course.
"""


from app.helper.helper_functions import read_conf, get_ed_align_additional_data


def build_metadata(data: dict) -> dict:
    """
    Creates a metadata dictionary for a single course. It distinguishes between the mandatory
    attributes and the optional.

    :param data: The input metadata to be enriched and restructured to fit the MOOChub format
    :type data: dict
    :return: A metadata dictionary conforming to the MOOChub metadata structure.
    :rtype: dict
    """
    publisher = build_organization_fragment(data["publisher"])
    creators = build_all_persons_fragments(data["creator"])

    metadata = {  # set of required attributes, minimum metadata according to MOOChub format
        "name": data["name"],
        "learningResourceType": build_resource_type_fragment(),
        "description": data["description"],  # Although it is not required by the MOOChub format, this program enforces
        # a description.
        "publisher": publisher,
        "creator": creators,
        "url": data["url"],
        "license": [data["license"]]
    }

    optional_attributes = {  # expendable to fit further optional attributes
        "startDate": build_date,
        "endDate": build_date,
        "educationalAlignment": build_all_educational_alignments,
        "teaches": build_all_teaches,
        "keywords": build_keywords,
        "educationalLevel": build_educational_level
    }

    for optional_attribute, fragment_function in optional_attributes.items():
        if optional_attribute in data.keys():
            metadata[optional_attribute] = fragment_function(data[optional_attribute])

    return metadata


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


def build_person_fragment(person_data: dict) -> dict:
    """
    Adds the mandatory "type" attribute to the person metadata fragment and sets it to "Person".

    :param person_data: A raw Person object.
    :type person_data: dict
    :return: A Organization object with the minimal requirements to conform with the MOOChub format.
    :rtype: dict
    """
    person_data["type"] = "Person"

    return person_data


def build_all_persons_fragments(persons: list) -> list:
    """
    Creates a list containing all Person metadata fragments based on a given list of raw person data.

    :param persons: A list with dictionaries containing the raw Person objects to be converted into the MOOChub format.
    :type persons: list
    :return: A list with MOOChub conform Person objects.
    :rtype: list
    """
    persons_metadata = list()

    for person in persons:
        persons_metadata.append(build_person_fragment(person))

    return persons_metadata


def build_educational_alignment_fragment(educational_alignment_data: dict) -> dict:
    """
    Takes a raw educationalAlignment object and enriches it with the mandatory data. It will take parts of the
    data from the respective configuration file connected to the given framework.

    :param educational_alignment_data: A dictionary with the raw "educationalAlignment" data.
    :type educational_alignment_data: dict
    :return: An "educationalAlignment" fragment conforming to the MOOChub format.
    :rtype: dict
    """
    framework = educational_alignment_data["educationalFramework"]

    conf = read_conf(framework, "educational_alignment")

    educational_alignment_data["alignmentType"] = "educationalSubject"
    educational_alignment_data["type"] = "EducationalAlignment"

    educational_alignment_data["educationalFrameworkVersion"] = conf["VERSION"]
    educational_alignment_data["url"] = conf["URL"]

    temp_name = educational_alignment_data["name"]

    name = [{
        "name": temp_name,
        "inLanguage": conf["LANGUAGE"]
    }]

    educational_alignment_data["name"] = name

    add_data = get_ed_align_additional_data(framework, temp_name)

    for attribute, value in add_data.items():
        educational_alignment_data[attribute] = value

    return educational_alignment_data


def build_all_educational_alignments(all_educational_data: list) -> list:
    """
    Creates a list of all "educationalAlignment" data fragments according to the MOOChub format. The basis is a list of
    raw educational alignment objects with the name and the framework of the educational alignment.

    :param all_educational_data: A list with raw "educationalAlignment" data (framework and educational alignment name).
    :type all_educational_data: list
    :return: A list of "educationalAlignment" data according to the MOOChub.
    :rtype: list
    """
    educational_alignment_metadata = list()

    for educational_data in all_educational_data:
        educational_alignment_metadata.append(build_educational_alignment_fragment(educational_data))

    return educational_alignment_metadata


def build_teaches_fragment(teaches_data: dict) -> dict:
    """
    Takes a raw teaches object and enriches it with the mandatory data. It will take parts of the
    data from the respective configuration file connected to the given framework.


    :param teaches_data: A raw "teaches" metadata fragment containing the name and the framework of a skill.
    :type teaches_data: dict
    :return: A "teaches" metadata fragment conforming to the MOOChub format.
    :rtype: dict
    """
    conf = read_conf(teaches_data["educationalFramework"], "teaches")

    teaches_data["educationalFrameworkVersion"] = conf["VERSION"]

    name = [{
        "name": teaches_data["name"],
        "inLanguage": conf["LANGUAGE"]
    }]

    teaches_data["name"] = name
    teaches_data["url"] = conf["URL"]

    return teaches_data


def build_all_teaches(teaches: list) -> list:
    """
    Creates a list of all "teaches" data fragments according to the MOOChub format. The basis is a list of
    raw educational alignment objects with the name and the framework of the skill/competency.

    :param teaches: A list with raw "teaches" data (framework and skill/competency name).
    :type teaches: list
    :return: A list of "teaches" data according to the MOOChub.
    :rtype: list
    """
    teaches_metadata = list()

    for teaches_fragment in teaches:
        teaches_metadata.append(build_teaches_fragment(teaches_fragment))

    return teaches_metadata


def build_date(date: str) -> list:
    """
    Puts the start date into a list. This is necessary to conform with the MOOChub format.

    :param date: A date (i.a. start or end date of a course).
    :type date: str
    :return: The date in a MOOChub conform way.
    :rtype: list
    """
    return [date]


def build_keywords(keywords: list) -> list:
    """
    Returns the keyword list. It is necessary because the build_metadata function expects a function to process the
    keywords.

    :param keywords: The list of keywords.
    :type keywords: list
    :return: The list of keywords.
    :rtype: list
    """
    return keywords


def build_educational_level(educational_level_data: dict) -> list:
    """
    Creates a MOOChub conform "educationalLevel" data fragment. Parts of the data are read from the respective
    configuration file as defined by the educational level framework.

    :param educational_level_data: A dictionary with the raw "educationalLevel" data (name, framework).
    :type educational_level_data: dict
    :return: A list with the MOOChub conform educationalLevel metadata fragment.
    :rtype: list
    """
    conf = read_conf(educational_level_data["educationalFramework"], "educational_level")

    educational_level_data["educationalFrameworkVersion"] = conf["VERSION"]

    name = [{
        "name": educational_level_data["name"],
        "inLanguage": conf["LANGUAGE"]
    }]

    educational_level_data["name"] = name

    educational_level_data["type"] = "EducationalLevel"

    return [educational_level_data]
