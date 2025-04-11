from app.helper.helper_functions import get_ed_align_framework_terms


PROMT = 'Given the title and description of a learning resource, find the corresponding ' \
            'topic or subject. Please use one of the provided terms for topics. Return the result as ' \
            '"educationalAlignment = <the term of the topic selected from the provided terms for topics>".\n'


def get_promt(framework):
    return f"{PROMT}\n"\
           f"Provided terms for topics: {get_ed_align_framework_terms(framework)}\n\n"
