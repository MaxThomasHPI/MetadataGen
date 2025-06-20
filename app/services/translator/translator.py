"""Translates a given text from German to English."""


import argostranslate.translate


from_code = "de"
to_code = "en"


def translate(text: str) -> str:
    """
    Translates an inputted text from German into English.

    :param text: The input text in german language.
    :type: str
    :return: The output text in English language.
    :rtype: str
    """
    translated = argostranslate.translate.translate(text, from_code, to_code)

    return translated
