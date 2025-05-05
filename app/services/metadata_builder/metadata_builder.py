from app.helper.helper_functions import read_conf, get_ed_align_additional_data


def build_metadata(data):
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

    optional_attributes = {
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


def build_resource_type_fragment():
    resource_type = {
        "identifier": "https://w3id.org/kim/hcrt/course",
        "type": "Concept",
        "inScheme": "https://w3id.org/kim/hcrt/scheme"
    }

    return resource_type


def build_organization_fragment(org_data: dict):
    org_data["type"] = "Organization"

    return org_data


def build_person_fragment(person_data: dict):
    person_data["type"] = "Person"

    return person_data


def build_all_persons_fragments(persons: list):
    persons_metadata = list()

    for person in persons:
        persons_metadata.append(build_person_fragment(person))

    return persons_metadata


def build_educational_alignment_fragment(educational_alignment_data: dict):
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


def build_all_educational_alignments(all_educational_data: list):
    educational_alignment_metadata = list()

    for educational_data in all_educational_data:
        educational_alignment_metadata.append(build_educational_alignment_fragment(educational_data))

    return educational_alignment_metadata


def build_teaches_fragment(teaches_data: dict):
    conf = read_conf(teaches_data["educationalFramework"], "teaches")

    teaches_data["educationalFrameworkVersion"] = conf["VERSION"]

    name = [{
        "name": teaches_data["name"],
        "inLanguage": conf["LANGUAGE"]
    }]

    teaches_data["name"] = name

    return teaches_data


def build_all_teaches(teaches: list):
    teaches_metadata = list()

    for teaches_fragment in teaches:
        teaches_metadata.append(build_teaches_fragment(teaches_fragment))

    return teaches_metadata


def build_date(date):
    return [date]


def build_keywords(keywords: list):
    return keywords


def build_educational_level(educational_level_data: dict):
    conf = read_conf(educational_level_data["educationalFramework"], "educational_level")

    educational_level_data["educationalFrameworkVersion"] = conf["VERSION"]

    name = [{
        "name": educational_level_data["name"],
        "inLanguage": conf["LANGUAGE"]
    }]

    educational_level_data["name"] = name

    educational_level_data["type"] = "EducationalLevel"

    return [educational_level_data]
