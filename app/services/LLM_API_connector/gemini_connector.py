import google.generativeai as genai
import os


def start_query(query):
    model = genai.GenerativeModel('gemini-1.5-flash')
    genai.configure(api_key=os.environ["GEMINI_KEY"])

    response = model.generate_content(query)
    text = response.text

    return text


