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
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])  # TODO: .env vs environ key, via config maybe?
    response = client.models.generate_content(
        model='gemini-2.5-flash-lite', contents=query
    )

    return response.text
