import os
import pandas as pd


def read_conf(framework, group):
    path = os.path.join(os.path.dirname(__file__), "../frameworks/" + group + "/" + framework + "/.conf")

    with open(path, 'r') as f:
        lines = f.readlines()

    return {line.split("=")[0]: line.split("=")[1][:-1] for line in lines}  # [:-1] removes newline "\n"


def get_DigComp_level():
    path = "../frameworks/educational_level/DigComp/DigComp.csv"

    full_path = os.path.join(os.path.dirname(__file__) + path)

    return pd.read_csv(full_path, index_col="DigComp_level")


def get_DigComp_level_name(level: int):
    dig_comp = get_DigComp_level()

    return dig_comp[dig_comp.index == level]["name"].item()


def get_DigComp_level_description(level: int):
    dig_comp = get_DigComp_level()

    return dig_comp[dig_comp.index == level]["explanation"].item()  # For this purpose we need a more
    # generalized description. The detailed description of the DigComp level is aligned with a specific competence.


def get_ed_align_framework(framework):
    path = f"../frameworks/educational_alignment/{framework}/{framework}.csv"
    full_path = os.path.join(os.path.dirname(__file__), path)

    return pd.read_csv(full_path, sep=";", dtype=str)


def get_ed_align_framework_terms(framework):
    terms = get_ed_align_framework(framework)
    max_level = max(terms["ShortCode"].str.len())

    return str(list(set(terms[terms["ShortCode"].str.len() == max_level]["Name"])))


def get_teaches_framework(framework):
    path = f"../frameworks/teaches/{framework}/{framework}.csv"
    full_path = os.path.join(os.path.dirname(__file__), path)

    return pd.read_csv(full_path, sep=";", dtype=str)


def get_teaches_framework_terms(framework):
    terms = get_teaches_framework(framework)
    max_level = max(terms["ShortCode"].str.len())

    return terms[terms["ShortCode"].str.len() == max_level][["Name", "Description"]]


def get_educational_level_framework(framework):
    path = f"../frameworks/educational_level/{framework}/{framework}.csv"
    full_path = os.path.join(os.path.dirname(__file__), path)

    return pd.read_csv(full_path, sep=";", dtype=str, index_col="Level")


def prepare_data(data):
    rows = list()
    for i, row in data.iterrows():
        rows.append((row["Level"], row["Name"]))
    return rows


def convert_table_into_tree(data, raw_data):
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


def find_leafs(tree: dict, leafs: list):
    for key, value in tree.items():
        if not value:
            leafs.append(key)
        else:
            find_leafs(value, leafs)


def add_data_to_leafs(tree, parent, data):
    for key, value in tree.items():
        if not value:
            value.update({
                "shortCode": data[(data["Name"] == key) & (data["Level"] == data["Level"].max()) &
                                  (data["BroaderConcept"] == parent)]["ShortCode"].iloc[0]
            })
        else:
            add_data_to_leafs(value, key, data)

