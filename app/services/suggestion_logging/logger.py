from datetime import datetime
import os


def log_suggestion(course_title, course_description, suggestion_type, framework, suggestions):
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

    with open(os.path.join(os.path.dirname(__file__), "log.csv"), 'a') as f:
        f.write(f"{index},{timestamp},{course_title},{course_description},{suggestion_type},{framework},{suggestions}\n")
