from app.services.queries.query_builder import create_query
from app.services.promter.promter_selector import select_single_promter
from app.services.LLM_API_connector.gemini_connector import start_query
from app.services.metadata_builder.metadata_builder import build_all_educational_alignments, build_all_teaches, \
    build_educational_level
from app.services.response_processor.data_extractor import extract_data


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
