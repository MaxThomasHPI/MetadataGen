"""
Helps to process provided frameworks in .CSV format.
"""


import os
import pandas as pd


def read_conf(framework: str, group: str) -> dict:
    """
    Reads teh configuration file of a framework and returns the variables and values as a dictionary.

    :param framework: The framework the config is for.
    :type: str
    :param group: The group (attribute) the framework is for (e.g. teaches, educational_alignment,...).
    :type group: str
    :return: The conf in the form of a dictionary.
    :rtype: dict
    """
    path = os.path.join(os.path.dirname(__file__), "../frameworks/" + group + "/" + framework + "/.conf")

    with open(path, 'r') as f:
        lines = f.readlines()

    return {line.split("=")[0]: line.split("=")[1][:-1] for line in lines}  # [:-1] removes newline "\n"


def get_ed_align_framework(framework: str) -> pd.DataFrame:
    """
    Reads and returns the requested educational alignment framework data as a pandas DataFrame.

    :param framework: The name of the framework.
    :type framework: str
    :return: The Framework as a pandas DataFrame.
    :rtype: pandas.DataFrame
    """
    path = f"../frameworks/educational_alignment/{framework}/{framework}.csv"
    full_path = os.path.join(os.path.dirname(__file__), path)

    return pd.read_csv(full_path, sep=";", dtype=str)


def get_ed_align_framework_terms(framework: str) -> str:
    """
    Reads all terms from an educational alignment framework but only shows the last entries (leaf nodes) if the
    framework is hierarchical. The leaf nodes are detected by the length of the short code.

    :param framework: The name of the Framework.
    :type framework: str
    :return: A string representation of a list. The list contains the terms that can be selected from the framework.
    :rtype: str
    """
    terms = get_ed_align_framework(framework)
    max_level = max(terms["ShortCode"].str.len())

    return str(list(set(terms[terms["ShortCode"].str.len() == max_level]["Name"])))


def get_ed_align_additional_data(framework: str, name: str) -> dict:
    """
    Retrieves additional data to a given educational alignment entry. This includes the URI (if available) and the
    hort code.

    :param framework: The name of the educational alignment framework.
    :type framework: str
    :param name: The name of the entry (educational alignment).
    :type name: str
    :return: A dictionary containing data about the URI and the short code of the entry.
    :rtype: dict
    """
    data = get_ed_align_framework(framework)
    data = data[data["Name"] == name]

    try:
        index = max(data.index)
    except ValueError:
        print("Value error!")
        print(f"Name: {name} \t Framework: {framework}")
        return {}

    data = data[data.index == index]

    return {"targetUrl": data["Uri"].item(), "shortCode": data["ShortCode"].item()}


def get_teaches_framework(framework: str) -> pd.DataFrame:
    """
    Reads and returns the requested teaches framework data as a pandas DataFrame.

    :param framework: The name of the framework.
    :type framework: str
    :return: The framework as a pandas DataFrame.
    :rtype: pandas.DataFrame
    """
    path = f"../frameworks/teaches/{framework}/{framework}.csv"
    full_path = os.path.join(os.path.dirname(__file__), path)

    return pd.read_csv(full_path, sep=";", dtype=str)


def get_teaches_framework_terms(framework: str) -> pd.DataFrame:
    """
    Reads all terms from a teaches framework but only shows the last entries (leaf nodes) if the framework is
    hierarchical. The leaf nodes are detected by the length of the short code.

    :param framework: The name of the framework.
    :type framework: str
    :return: A pandas DataFrame containing the names and descriptions of the teaches entries.
    :rtype: pandas.DataFrame
    """
    terms = get_teaches_framework(framework)
    max_level = max(terms["ShortCode"].str.len())

    return terms[terms["ShortCode"].str.len() == max_level][["Name", "Description"]]


def get_educational_level_framework(framework: str) -> pd.DataFrame:
    """
    Reads and returns the requested educational level framework data as a pandas DataFrame.

    :param framework: The name of the framework.
    :type framework: str
    :return: The framework as a pandas DataFrame.
    :rtype: pd.DataFrame
    """
    path = f"../frameworks/educational_level/{framework}/{framework}.csv"
    full_path = os.path.join(os.path.dirname(__file__), path)

    return pd.read_csv(full_path, sep=";", dtype=str, index_col="Level")


def prepare_data(data: pd.DataFrame) -> list:
    """
    Convert a framework DataFrame into a list of tuples containing the level and the name for each entry.

    :param data: A DataFrame containing a framework.
    :type data: pandas.DataFrame
    :return: A list of tuples containing the level and the name of each entry of the given framework.
    :rtype: list
    """
    rows = list()
    for i, row in data.iterrows():
        rows.append((row["Level"], row["Name"]))
    return rows


def convert_table_into_tree(data: pd.DataFrame, raw_data: pd.DataFrame) -> dict:
    """
    Converts a framework table (pandas DataFrame) into a tree-structured dictionary.

    :param data: The framework that wil be converted.
    :type data: pandas.DataFrame
    :param raw_data: The framework again. This will be used as a source for enriching the tree with data.
    :type raw_data: pandas.DataFrame
    :return: A framework converted into a tree-structure.
    :rtype: dict
    """
    data = prepare_data(data)

    tree = dict()
    stack = []

    for level, name in data:
        node = {name: {}}

        if not stack:
            tree.update(node)
            stack.append((level, node))
            continue

        while stack and stack[-1][0] >= level:
            stack.pop()

        if stack:
            parent = list(stack[-1][1].values())[0]
            parent.update(node)
        else:
            tree.update(node)

        stack.append((level, node))

    add_data_to_leafs(tree, None, raw_data)

    return tree


def add_data_to_leafs(tree: dict, parent: str | None, data: pd.DataFrame) -> None:
    """
    Adds short codes to leaf nodes. This ensures that the information is present when the metadata is build.

    :param tree: A framework converted into a tree-structure.
    :type tree: dict
    :param parent: The name of the parent entry if existent.
    :type parent: str
    :param data: The original framework data for enriching the data stored in the leafs.
    :type data: pandas.DataFrame
    """
    for key, value in tree.items():
        if not value:
            value.update({
                "shortCode": data[(data["Name"] == key) & (data["Level"] == data["Level"].max()) &
                                  (data["BroaderConcept"] == parent)]["ShortCode"].iloc[0]
            })
        else:
            add_data_to_leafs(value, key, data)
