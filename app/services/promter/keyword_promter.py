#import json

PROMT = 'Based on the title and description of the learning resource, give me 10 keywords that ' \
        'describe that paragraph best. The keywords must be common terms that everyone can understand. ' \
        'A keyword may also consist of multiple words. Return the result in form of an Python list ' \
        'following the pattern "keywords = <the list with the keywords>".\n\n'


def get_promt():
    return PROMT


"""
def extract_data(raw_data: str):
    keywords = raw_data.strip("\n").split("= ")[1]
    keywords = json.loads(keywords)
    keywords.sort()

    return keywords
"""