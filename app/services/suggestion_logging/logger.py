"""
Logs and tracks suggestions made by the suggestion engine and saves them to a CSV
file. This log file can later be used to evaluate the quality of the suggestions
and to improve this program.
"""


from datetime import datetime
import os


def log_suggestion(course_title: str, course_description: str, suggestion_type: str, framework: str, suggestions: str) \
        -> None:
    """
    Creates a log entry and saves it to a CSV file (log file). The log includes the
    course title and description for identification of the course. It will create a
    time stamp when the entry is created. The suggestion type (attribute) will be
    saved together with the framework used. The actual suggestions will be saved as
    a string representation.

    :param course_title: The title/name of a course.
    :type course_title: str
    :param course_description: The description of the course.
    :type course_description: str
    :param suggestion_type: The attribute for which the suggestion is made.
    :type suggestion_type: str
    :param framework: The framework used for the suggestion.
    :type framework: str
    :param suggestions: The suggestions made by the program.
    :type suggestions: str
    """
    if "log.csv" not in os.listdir(os.path.dirname(__file__)):
        header = ",timestamp,course_title,course_description,suggestion_type,framework,suggestions\n"
        with open(os.path.join(os.path.dirname(__file__), "log.csv"), 'w') as f:
            f.write(header)

    with open(os.path.join(os.path.dirname(__file__), "log.csv"), 'r') as f:
        logs = f.readlines()

    if len(logs) == 1:
        index = 0
    else:
        index = int(logs[-1].split(",")[0]) + 1

    timestamp = str(datetime.now())
    course_description = '"' + course_description.replace("\n", "") + '"'

    with open(os.path.join(os.path.dirname(__file__), "log.csv"), 'a') as f:
        f.write(f"{index},{timestamp},{course_title},{course_description},{suggestion_type},{framework},"
                f"{suggestions}\n")
