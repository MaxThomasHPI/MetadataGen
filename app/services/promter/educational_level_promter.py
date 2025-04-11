from app.helper.helper_functions import get_educational_level_framework


def get_promt(framework):
    promt = 'Please give a rating for the difficulty of a learning resource based on the title and the ' \
            'description. Please use the given framework under level_framework and assign ' \
            'the appropriate level. The level is the term or number in the "Level" column. Please ' \
            'select the appropriate level according to the "explanation" column. Return the results ' \
            'in this form: "educationalLevel = <the level you picked according to the framework>".\n'

    return f"{promt}\n" \
           f"level_framework: {get_educational_level_framework(framework)}\n\n"
