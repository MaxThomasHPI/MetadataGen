from app.services.queries.query_builder import create_query
from app.services.promter.promter_selector import select_single_promter
from app.services.LLM_API_connector.gemini_connector import start_query
from app.services.metadata_builder.metadata_builder import build_all_educational_alignments, build_all_teaches, \
    build_educational_level
from app.services.response_processor.data_extractor import extract_data
from app.services.ESCO_suggestion_engine.ESCO_suggestion_engine import find_skills
from app.services.suggestion_logging.logger import log_suggestion


def generate_ed_align_suggestion(title, description, framework, suggestion=None):
    if not suggestion:
        promter = select_single_promter('ed_align')
        promts = [promter.get_promt(framework)]

        query = create_query(title, description, promts)

        suggestion = extract_data(start_query(query))

    suggestion = suggestion["educationalAlignment"]

    temp = [{
        "name": suggestion,
        "educationalFramework": framework
    }]

    log_suggestion(title, description, "edAlign", framework, suggestion)

    return build_all_educational_alignments(temp)


def generate_teaches_suggestion(title, description, framework, suggestion=None):
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


def generate_keywords_suggestion(title, description, suggestion=None):
    if not suggestion:
        promter = select_single_promter('keywords')
        promts = [promter.get_promt()]

        query = create_query(title, description, promts)

        suggestion = start_query(query)
        suggestion = extract_data(suggestion)

    for_logging = ",".join(suggestion["keywords"])
    log_suggestion(title, description, "keywords", "", for_logging)

    return suggestion


def generate_educational_level_suggestion(title, description, framework, suggestion=None):
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


def generate_specified_suggestions(title: str, description: str, services: dict):
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
            metadata_fragments[key] = generate_ed_align_suggestion(title, description,
                                                                   framework, suggestion)
        elif key == "keywords":
            metadata_fragments[key] = generate_keywords_suggestion(title, description,
                                                                   suggestion)
        elif key == "teaches":
            framework = services["teaches"]
            metadata_fragments[key] = generate_teaches_suggestion(title, description,
                                                                  framework, suggestion)
        elif key == "educationalLevel":
            framework = services["educational_level"]
            metadata_fragments[key] = generate_educational_level_suggestion(title,
                                                                            description,
                                                                            framework,
                                                                            suggestion)["educationalLevel"]
        else:
            continue

    return metadata_fragments


def generate_esco_suggestion(title, description):
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
