import requests
from app.services.translator.translator import translate


def load_dataset(url):
    return requests.get(url).json()


def extract_course(data, short_code):
    courses = data["data"]

    for course in courses:
        if course["attributes"]["courseCode"] == short_code:
            return course

    return None


def find_dataset(short_code):
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
