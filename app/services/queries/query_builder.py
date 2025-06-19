"""Assembles all promts into a single query for the LLM."""


PROMT = "You are asked to create metadata for a learning resource.\n"


def create_query(title: str, description: str, promts: list = None) -> str:
    """
    Creates a query based on the title, description, and promts to be passed to a LLM.

    :param title: The title of a course.
    :type title: str
    :param description: The description of a course.
    :type description: str
    :param promts: A list of promts to be added to the query.
    :type promts: list
    :return: A query to be passed to the LLM.
    :rtype: str
    """
    query = PROMT

    for p in promts:
        query += p

    query += f"title: {title}\n" \
             f"description: {description}"

    return query
