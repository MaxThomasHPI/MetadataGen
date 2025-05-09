from app.services.queries.query_builder import create_query
from app.services.promter.promter_selector import select_single_promter
from app.services.LLM_API_connector.gemini_connector import start_query
from app.services.metadata_builder.metadata_builder import build_all_educational_alignments, build_all_teaches, \
    build_educational_level
from app.services.response_processor.data_extractor import extract_data
from app.services.ESCO_suggestion_engine.ESCO_suggestion_engine import find_skills


def generate_ed_align_suggestion(title, description, framework):
    promter = select_single_promter('ed_align')
    promts = [promter.get_promt(framework)]

    query = create_query(title, description, promts)

    suggestion = extract_data(start_query(query))["educationalAlignment"]

    temp = [{
        "name": suggestion,
        "educationalFramework": framework
    }]

    return build_all_educational_alignments(temp)


def generate_teaches_suggestion(title, description, framework):
    promter = select_single_promter('teaches')
    promts = [promter.get_promt(framework)]

    query = create_query(title, description, promts)

    suggestion = extract_data(start_query(query))["teaches"]
    all_suggestions = list()

    for competency in suggestion.keys():
        temp = {
            "educationalFramework": framework,
            "name": competency
        }
        all_suggestions.append(temp)

    return build_all_teaches(all_suggestions)


def generate_keywords_suggestion(title, description):
    promter = select_single_promter('keywords')
    promts = [promter.get_promt()]

    query = create_query(title, description, promts)

    suggestion = start_query(query)

    return extract_data(suggestion)


def generate_educational_level_suggestion(title, description, framework):
    promter = select_single_promter('educational_level')
    promts = [promter.get_promt(framework)]

    query = create_query(title, description, promts)

    suggestion = extract_data(start_query(query))

    temp = {
        "name": suggestion["educationalLevel"],
        "educationalFramework": framework
    }

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
            temp = [{
                "name": value,
                "educationalFramework": framework
            }]
            metadata_fragments[key] = build_all_educational_alignments(temp)
        elif key == "keywords":
            metadata_fragments[key] = value
        elif key == "teaches":
            framework = services["teaches"]
            all_suggestions = list()

            for competency in value.keys():
                temp = {
                    "educationalFramework": framework,
                    "name": competency
                }
                all_suggestions.append(temp)

            metadata_fragments[key] = build_all_teaches(all_suggestions)
        elif key == "educationalLevel":
            framework = services["educational_level"]
            temp = {
                "name": value,
                "educationalFramework": framework
            }

            metadata_fragments[key] = build_educational_level(temp)
        else:
            continue

    return metadata_fragments


def generate_esco_suggestion(title, description):
    query = f"{title}. {description}"

    skills = find_skills(query)

    metadata_fragments = list()
    for skill in skills:
        metadata_fragments.append({
            "name": skill["title"],
            "conceptUrl": skill["uri"],
            "educationalFramework": "ESCO"
        })

    return build_all_teaches(metadata_fragments)
