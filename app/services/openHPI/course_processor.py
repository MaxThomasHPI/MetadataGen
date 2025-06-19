"""
Loads and preprocesses existing course metadata of openHPI courses. The courses are loaded from openHPI's MOOChub API.
This API already provides MOOChub format conform metadata but certain optional attributes might be missing.
"""


import requests
from app.services.translator.translator import translate


def load_dataset(url: str) -> dict:
    """
    Loads a set of course metadata from openHPI's MOOChub API based on a URL. A whole page with up to 50 courses and the
    pagination information ("links") is loaded. The result needs to be processed further to get the metadata of a single
    course.

    :param url: The URL to a page with the openHPI course metadata.
    :type url: str
    :return: A dictionary with the metadata of up to 50 courses loaded from the defined endpoint.
    :rtype: dict
    """
    return requests.get(url).json()


def extract_course(data: dict, short_code: str) -> dict | None:
    """
    Extracts a metadata set of a single course. The course is defined by its short code. If the short code is not found
    in metadat set it returns None.

    :param data: A page of the data containing the metadata of up to 50 courses.
    :type data: dict
    :param short_code: The short code of a course to be found in ht metadata set.
    :type short_code: str
    :return: The course metadata as a dictionary if found and None for else.
    :rtype: dict | None
    """
    courses = data["data"]

    for course in courses:
        if course["attributes"]["courseCode"] == short_code:
            return course

    return None


def find_dataset(short_code: str) -> dict | None:
    """
    Finds and extracts the metadata of a course specified by its short code. It will return None if the course does
    not exist. It the course is given in German it will translate the description and the title into English.

    :param short_code: The short code identifying the course.
    :type short_code: str
    :return: A metadata set of the extracted course or None if no course with the short code could be found.
    :rtype: dict | None
    """
    url = "https://open.hpi.de/bridges/moochub/courses"

    data = load_dataset(url)

    current_page = int(data["links"]["self"].split("=")[1])
    max_page = int(data["links"]["last"].split("=")[1])

    course = extract_course(data, short_code)

    while not course and current_page < max_page:

        url = data["links"]["next"]

        data = load_dataset(url)
        course = extract_course(data, short_code)

        current_page = int(data["links"]["self"].split("=")[1])

    if course and course["attributes"]["inLanguage"][0] == "de":
        course["attributes"]["name"] = translate(course["attributes"]["name"])
        course["attributes"]["description"] = translate(course["attributes"]["description"])

    return course
