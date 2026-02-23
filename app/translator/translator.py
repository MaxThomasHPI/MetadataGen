import argostranslate.translate
from langdetect import detect, LangDetectException


from_code = "de"
to_code = "en"


def translate(text: str) -> str:
    """
    Translates an inputted text from German into English if the text is identified
    to be in German. Otherwise, the text is returned unchanged.

    :param text: The input text ot be checked and translated if needed.
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
