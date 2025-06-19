"""Creates the promt for generating the educationalAlignment attribute suggestion"""


from app.helper.helper_functions import get_ed_align_framework_terms


PROMT = 'Given the title and description of a learning resource, find the corresponding ' \
            'topic or subject. Please use one of the provided terms for topics. Return the result as ' \
            '"educationalAlignment = <the term of the topic selected from the provided terms for topics>".\n'


def get_promt(framework: str) -> str:
    """
    Provides the promt the educationalAlignment attribute suggestion. It will pass a set of predefined terms to the LLM
    based on the specified framework.

    :param framework: The framework that is used for the suggestion.
    :type framework: str
    :return: A promt for generating the suggestion including the vocabulary that shall be used.
    :rtype: str
    """
    return f"{PROMT}\n"\
           f"Provided terms for topics: {get_ed_align_framework_terms(framework)}\n\n"
