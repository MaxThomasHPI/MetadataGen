"""
Translates a given text from German to English. This happens only when the inputted
text is identified as a text written in German.
"""


import argostranslate.translate
from langdetect import detect, LangDetectException


from_code = "de"
to_code = "en"


def translate(text: str) -> str:
    """
    Translates an inputted text from German into English if the text is identified
    to be in German.

    :param text: The input text in german language.
    :type: str
    :return: The output text in English language.
    :rtype: str
    """
    try:
        if detect(text) == from_code:
            translated = argostranslate.translate.translate(text, from_code, to_code)
        else:
            translated = text
    except LangDetectException as e:
        translated = ""
        print("Error:", e)

    return translated
