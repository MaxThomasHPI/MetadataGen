import argostranslate.translate


from_code = "de"
to_code = "en"


def translate(text):
    translated = argostranslate.translate.translate(text, from_code, to_code)

    return translated
