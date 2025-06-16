"""Executes queries against a GEMINI instance."""


import google.generativeai as genai
import os


def start_query(query: str) -> str:
    """
    Fires a query against a Google's GEMINI API. Currently, only the model GEMINI Flash 1.5 is supported.

    :param query: The query to be fired against the API.
    :type query: str
    :return: A response text as answer for the query.
    :rtype: str
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    genai.configure(api_key=os.environ["GEMINI_KEY"])

    response = model.generate_content(query)
    text = response.text

    return text
