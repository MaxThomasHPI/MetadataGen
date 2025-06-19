"""Creates the promt for generating the teaches attribute suggestion"""


from app.helper.helper_functions import get_teaches_framework_terms, get_educational_level_framework


PROMT = 'Please check the provided title and description. Select the corresponding ' \
            'competencies that are taught in this course. Take only the competencies from the provided ' \
            '"competencies_framework" DataFrame in the column "Name". Limit this selection to the four ' \
            'most prominent competencies taught in the course. For selecting the competencies, please use the ' \
            '"Description" column for a more detailed description of what a competency entails. Determine a ' \
            'difficulty level for each competency according to the level system as provided in the "level_framework" ' \
            'DataFrame. Please return the results only in the following format: teaches = <the four selected ' \
            'competencies in the style of a Python dictionary with the competency name as provided in the ' \
            'competency DataFrame in the column "Name" the key and the competency level as the value (integer)>.' \
            '\nEXAMPLE OUTPUT YOU WILL RETURN:\n' \
            'teaches = {<Name>: <level>, <Name>: <level>, <Name>: <level>, <Name>: <level>}\n' \
            '\nYou will NOT return a code, just your choices in the given format.\n'


def get_promt(framework: str) -> str:
    """
    Provides the promt the teaches attribute suggestion. It will pass a set of predefined terms to the LLM
    based on the specified framework.

    :param framework: The framework that is used for the suggestion.
    :type framework: str
    :return: A promt for generating the suggestion including the vocabulary that shall be used.
    :rtype: str
    """
    return f"{PROMT}\n" \
           f"competencies_framework: {get_teaches_framework_terms(framework)}\n" \
           f"level_framework: {get_educational_level_framework(framework)}\n"
