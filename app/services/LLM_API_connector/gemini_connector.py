"""Executes queries against a GEMINI instance."""


from google import genai
import os


def start_query(query: str) -> str:
    """
    Fires a query against a Google's GEMINI API. Currently, only the model GEMINI 2.0 Flash is supported.

    :param query: The query to be fired against the API.
    :type query: str
    :return: A response text as answer for the query.
    :rtype: str
    """
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=query
    )

    text = response.text

    return text
