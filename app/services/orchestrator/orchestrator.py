"""
Manages the selection of promters for the respective task e.g. generate a suggestion for the educationalAlignment
attribute, etc.
"""


from app.services.queries.query_builder import create_query
from app.services.promter.promter_selector import select_single_promter
from app.services.LLM_API_connector.gemini_connector import start_query
from app.services.metadata_builder.metadata_builder import build_all_educational_alignments, build_all_teaches, \
    build_educational_level
from app.services.response_processor.data_extractor import extract_data
from app.services.ESCO_suggestion_engine.ESCO_suggestion_engine import find_skills
from app.services.suggestion_logging.logger import log_suggestion
from app.services.translator.translator import translate


def generate_ed_align_suggestion(title: str, description: str, framework: str, suggestion: dict = None) -> list:
    """
    Generates a suggestion for an educational alignment for the course. Only one EducationalAlignment fragment will be
    generated. This function will just convert an existing suggestion into the MOOChub format if provided via the
    "suggestion" parameter.

    :param title: The title of the course.
    :type title: str
    :param description: The description of the course.
    :type description: str
    :param framework: The framework to be used for the suggestion.
    :type framework: str
    :param suggestion: An existing suggestion.
    :type suggestion: dict
    :return: A list of suggested educational alignments for the course.
    :rtype: list
    """
    if not suggestion:
        promter = select_single_promter('ed_align')
        promts = [promter.get_promt(framework)]

        query = create_query(title, description, promts)

        suggestion = extract_data(start_query(query))

    try:
        suggestion = suggestion["educationalAlignment"]
    except KeyError:
        print("Key error!")
        print(title)
        print(suggestion)
        suggestion = ""

    temp = [{
        "name": suggestion,
        "educationalFramework": framework
    }]

    log_suggestion(title, description, "edAlign", framework, suggestion)

    return build_all_educational_alignments(temp)


def generate_teaches_suggestion(title: str, description: str, framework: str, suggestion: dict = None) -> list:
    """
    Generates suggestions for skills/competencies for the course. Four Skill fragments will be generated and returned
    as a list. This function will just convert an existing suggestion into the MOOChub format if provided via the
    "suggestion" parameter.

    :param title: The title of the course.
    :type title: str
    :param description: The description of the course.
    :type description: str
    :param framework: The framework to be used for the suggestion.
    :type framework: str
    :param suggestion: An existing suggestion.
    :type suggestion: dict
    :return: A list of suggested skills/competencies for the course.
    :rtype: list
    """
    if not suggestion:
        promter = select_single_promter('teaches')
        promts = [promter.get_promt(framework)]

        query = create_query(title, description, promts)

        suggestion = extract_data(start_query(query))

    suggestion = suggestion["teaches"]
    all_suggestions = list()

    for_logging = ""

    for competency in suggestion.keys():
        temp = {
            "educationalFramework": framework,
            "name": competency
        }
        all_suggestions.append(temp)
        for_logging += competency

    log_suggestion(title, description, "teaches", framework, for_logging)

    return build_all_teaches(all_suggestions)


def generate_keywords_suggestion(title: str, description: str, suggestion: dict = None) -> list:
    """
    Generates suggestions for keywords for the course. Ten suggestions will be generated and returned as a list. This
    function will just convert an existing suggestion into the MOOChub format if provided via the "suggestion"
    parameter.

    :param title: The title of the course.
    :type title: str
    :param description: The description of the course.
    :type description: str
    :param suggestion: An existing suggestion.
    :type suggestion: dict
    :return: A list of suggested keywords for the course.
    :rtype: list
    """
    if not suggestion:
        promter = select_single_promter('keywords')
        promts = [promter.get_promt()]

        query = create_query(title, description, promts)

        suggestion = start_query(query)
        suggestion = extract_data(suggestion)

    for_logging = ",".join(suggestion["keywords"])
    log_suggestion(title, description, "keywords", "", for_logging)

    return suggestion


def generate_educational_level_suggestion(title: str, description: str, framework: str, suggestion: dict = None) \
        -> dict:
    """
    Generates a suggestion for the educational level of the course. This function will just convert an existing
    suggestion into the MOOChub format if provided via the "suggestion" parameter.

    :param title: The title of the course.
    :type title: str
    :param description: The description of the course.
    :type description: str
    :param framework: The framework to be used for the suggestion.
    :type framework: str
    :param suggestion: An existing suggestion.
    :type suggestion: dict
    :return: A EducationalLevel fragment.
    :rtype: dict
    """
    if not suggestion:
        promter = select_single_promter('educational_level')
        promts = [promter.get_promt(framework)]

        query = create_query(title, description, promts)

        suggestion = extract_data(start_query(query))

    temp = {
        "name": suggestion["educationalLevel"],
        "educationalFramework": framework
    }

    log_suggestion(title, description, "educational_level", framework, suggestion["educationalLevel"])

    return {"educationalLevel": build_educational_level(temp)}


def generate_specified_suggestions(title: str, description: str, services: dict) -> dict:
    """
    Generates suggestions based on the defined services for the course.

    :param title: The title of the course.
    :type title: str
    :param description: The description of the course.
    :type description: str
    :param services: The services and the corresponding framework to be used for the service.
    :type services: dict
    :return: The generated suggested metadata fragments according to the MOOChub format.
    :rtype: dict
    """
    metadata_fragments = dict()
    promts = list()

    for key, value in services.items():
        promter = select_single_promter(key)
        if value:
            promts.append(promter.get_promt(value))
        else:
            promts.append(promter.get_promt())

    query = create_query(title, description, promts)

    suggestion = extract_data(start_query(query))

    for key, value in suggestion.items():
        if key == "educationalAlignment":
            framework = services["ed_align"]
            metadata_fragments[key] = generate_ed_align_suggestion(title, description, framework, suggestion)
        elif key == "keywords":
            metadata_fragments[key] = generate_keywords_suggestion(title, description, suggestion)
        elif key == "teaches":
            framework = services["teaches"]
            metadata_fragments[key] = generate_teaches_suggestion(title, description, framework, suggestion)
        elif key == "educationalLevel":
            framework = services["educational_level"]
            metadata_fragments[key] = generate_educational_level_suggestion(title, description, framework,
                                                                            suggestion)["educationalLevel"]
        else:
            continue

    return metadata_fragments


def generate_esco_suggestion(title: str, description: str) -> list:
    """
    Generates a teaches suggestion according to the ESCO framework. Four skills/competencies will be generated.

    :param title: The title of the course.
    :type title: str
    :param description: The description of the course.
    :type description: str
    :return: A list of the suggested ESCO skills/competencies for the course.
    :rtype: list
    """
    title = translate(title)
    description = translate(description)

    query = f"{title}. {description}"

    skills = find_skills(query)

    metadata_fragments = list()
    for_logging = list()

    for skill in skills:
        metadata_fragments.append({
            "name": skill["title"],
            "conceptUrl": skill["uri"],
            "educationalFramework": "ESCO"
        })
        for_logging.append(skill["title"])

    for_logging = ",".join(for_logging)
    log_suggestion(title, description, "teaches", "ESCO", for_logging)

    return build_all_teaches(metadata_fragments)
