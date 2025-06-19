"""Selects the specified promter or all promters to generate the respective promts for the LLM."""


import types
from app.services.promter import keyword_promter, educational_level_promter, educational_alignment_promter, \
    teaches_promter


def select_all() -> list:
    """
    Selects the references on all available promters and returns them as a list.

    :return: A list references on all available promters.
    :rtype: list
    """
    return [keyword_promter, educational_alignment_promter, educational_level_promter, teaches_promter]


def select_single_promter(promter_name: str) -> types.ModuleType | None:
    """
    Selects a promter according to the queried attribute.

    :param promter_name: The name of the attribute the promter is for.
    :type promter_name: str
    :return: The reference on the selected promter.
    :rtype: types.ModuleType
    """
    if promter_name == "ed_align":
        return educational_alignment_promter
    elif promter_name == "teaches":
        return teaches_promter
    elif promter_name == "keywords":
        return keyword_promter
    elif promter_name == "educational_level":
        return educational_level_promter
    else:
        return None
