"""
Finds all absolute paths to the .CSV files containing the framework data.
The relevant data from the frameworks is extracted by the gather_all_framework_data,
extract_relevant_data, and gather_all_educational_level_data.
The functions can distinguish between the .CSV file stored data and the ESCO graph.
"""


import os
import pandas as pd
from app.helper.helper_functions import read_conf, convert_table_into_tree
from app.services.ESCO_processor.ESCO_processor import get_initial_data


def find_all_framework_paths(purpose: str) -> list:
    """
    Returns a list of strings representing the absolute paths to the files (.CSV)
    that store the framework data.

    :param purpose: The purpose (attribute) of the framework (e.g. teaches,
    educationalAlignment).
    :type purpose: str
    :return: A list of all absolute paths to the .CSV files in the frameworks folder
    for the given purpose (attribute).
    :rtype: list
    """
    path = os.path.join(os.path.dirname(__file__), f"../../frameworks/{purpose}")
    framework_paths = list()

    for framework in os.listdir(path):
        framework_paths.append(f"{path}/{framework}/{framework}.csv")

    return framework_paths


def gather_all_framework_data(purpose: str) -> dict:
    """
    Gathers the data of all frameworks of a given purpose (attribute) like teaches
    and returns them in a dictionary for presenting to user, for example.

    :param purpose: The purpose (attribute) of the framework (e.g. teaches,
    educationalAlignment).
    :type purpose: str
    :return: A dictionary containing the framework data (entries) for  a given purpose
    (attribute)
    :rtype: dict
    """
    frameworks = find_all_framework_paths(purpose)

    data = dict()
    for framework in frameworks:
        framework_name = framework.split('/')[-1].split(".")[0]

        if framework_name == "ESCO":
            data[framework_name] = get_initial_data()
        else:
            data[framework_name] = extract_relevant_data(framework, purpose)

    return data


def extract_relevant_data(framework_path: str, purpose: str) -> dict:
    """
    Extracts th relevant data of a given framework (by the path where it is stored)
    and its purpose (attribute). The extracted data is returned as a dictionary
    containing the relevant framework data in a tree-structure.

    :param framework_path: The path to a .CSV file containing the framework data.
    :type framework_path: str
    :param purpose: The purpose (attribute) of the framework (e.g. teaches,
    educationalAlignment).
    :return: The relevant data of a framework in a tree-structure.
    :rtype: dict
    """
    conf = read_conf(framework_path.split('/')[-1].split(".")[0], purpose)

    raw_data = pd.read_csv(framework_path, sep=conf["SEP"], dtype=str)
    raw_data = raw_data.astype({"Level": int})

    data = raw_data[["Level", "Name"]]

    tree = convert_table_into_tree(data, raw_data)

    return tree


def gather_educational_level_data() -> dict:
    """
    Extracts all relevant data for the educationalLevel attribute from available
    frameworks in the respective folder.

    :return: The relevant data of all educationalLevel frameworks available.
    :rtype: dict
    """
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
