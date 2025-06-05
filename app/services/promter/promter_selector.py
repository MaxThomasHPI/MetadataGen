from app.services.promter import keyword_promter, educational_level_promter, educational_alignment_promter, \
    teaches_promter


def select_all():
    return [keyword_promter, educational_alignment_promter, educational_level_promter, teaches_promter]


def select_single_promter(promter_name):
    if promter_name == "ed_align":
        return educational_alignment_promter
    elif promter_name == "teaches":
        return teaches_promter
    elif promter_name == "keywords":
        return keyword_promter
    elif promter_name == "educational_level":
        return educational_level_promter
    else:
        return None
