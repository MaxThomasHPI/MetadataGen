import os
import pandas as pd
from app.helper.helper_functions import read_conf, convert_table_into_tree


def find_all_framework_paths(purpose):
    path = os.path.join(os.path.dirname(__file__), f"../../frameworks/{purpose}")
    framework_paths = list()

    for framework in os.listdir(path):
        framework_paths.append(f"{path}/{framework}/{framework}.csv")

    return framework_paths


def gather_all_framework_data(purpose):
    frameworks = find_all_framework_paths(purpose)

    data = dict()
    for framework in frameworks:
        framework_name = framework.split('/')[-1].split(".")[0]

        data[framework_name] = extract_relevant_data(framework, purpose)

    return data


def extract_relevant_data(framework_path, purpose):
    conf = read_conf(framework_path.split('/')[-1].split(".")[0], purpose)

    raw_data = pd.read_csv(framework_path, sep=conf["SEP"], dtype=str)
    raw_data = raw_data.astype({"Level": int})

    data = raw_data[["Level", "Name"]]

    tree = convert_table_into_tree(data, raw_data)

    return tree


def gather_educational_level_data():
    path = os.path.join(os.path.dirname(__file__), "../../frameworks/educational_level")

    frameworks = dict()

    for framework in os.listdir(path):
        framework_path = path + f"/{framework}/{framework}.csv"
        conf = read_conf(framework_path.split('/')[-1].split(".")[0], "educational_level")
        data = pd.read_csv(framework_path, sep=conf["SEP"])

        temp = list()
        for i, row in data.iterrows():
            temp.append({"name": row["Name"], "description": row["Description"], "level": row["Level"]})

        frameworks[framework] = temp

    return frameworks
