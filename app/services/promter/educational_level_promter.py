"""Creates the promt for generating the educationalLevel attribute suggestion"""


from app.helper.helper_functions import get_educational_level_framework


PROMT = 'Please give a rating for the difficulty of a learning resource based on the title and the ' \
            'description. Please use the given framework under level_framework and assign ' \
            'the appropriate level. The level is the term or number in the "Level" column. Please ' \
            'select the appropriate level according to the "explanation" column. Return the results ' \
            'in this form: "educationalLevel = <the level you picked according to the framework>".\n'


def get_promt(framework: str) -> str:
    """
    Provides the promt the educationalLevel attribute suggestion. It will pass a set of predefined terms to the LLM
    based on the specified framework.

    :param framework: The framework that is used for the suggestion.
    :type framework: str
    :return: A promt for generating the suggestion including the vocabulary that shall be used.
    :rtype: str
    """
    return f"{PROMT}\n" \
           f"level_framework: {get_educational_level_framework(framework)}\n\n"
