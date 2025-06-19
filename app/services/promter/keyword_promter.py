"""Creates the promt for generating the keywords attribute suggestion"""


PROMT = 'Based on the title and description of the learning resource, give me 10 keywords that ' \
        'describe that paragraph best. The keywords must be common terms that everyone can understand. ' \
        'A keyword may also consist of multiple words. Return the result in form of an Python list ' \
        'following the pattern "keywords = <the list with the keywords>".\n\n'


def get_promt() -> str:
    """
    Returns the promt for generating keywords suggestions.

    :return: A promt designed for the generation of keywords.
    :rtype: str
    """
    return PROMT
