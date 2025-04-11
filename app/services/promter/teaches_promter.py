from app.helper.helper_functions import get_teaches_framework_terms, get_educational_level_framework


PROMT = 'Please check the provided title and description. Select the corresponding ' \
            'competencies that are taught in this course. Take only the competencies from the provided ' \
            '"competencies_framework" DataFrame in the column "Name". Limit this selection to the four ' \
            'most prominent competencies taught in the course. For selecting the competencies, please use the ' \
            '"Description" column for a more detailed description of what a competency entails. Determine a ' \
            'difficulty level for each competency according to the level system as provided in the "level_framework" ' \
            'DataFrame. Please return the results only in the following format: teaches = <the four selected ' \
            'competencies in the style of a Python dictionary with the competency short code as provided in the ' \
            'competency DataFrame the key and the competency level as the value (integer)>.\n'


def get_promt(framework):
    return f"{PROMT}\n" \
           f"competencies_framework: {get_teaches_framework_terms(framework)}\n" \
           f"level_framework: {get_educational_level_framework(framework)}\n"
