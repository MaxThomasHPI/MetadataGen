from app.helper.paths import FRAMEWORK_ROOT
from app.framework_handler.framework_data_retriever import find_top_level_entries, find_sub_entries
from app.framework_handler.framework_helper import prepare_entry
import os


def list_all_frameworks():
    groups = os.listdir(FRAMEWORK_ROOT)

    frameworks = dict()

    for group in groups:
        path = (
            FRAMEWORK_ROOT /
            group
        )
        frameworks[group] = os.listdir(path)

    return frameworks


def list_all_frameworks_with_top_level_entries():
    frameworks = list_all_frameworks()

    top_level_entries = dict()
    for group, frameworks in frameworks.items():
        framework_entries = dict()
        for framework in frameworks:
            entries = find_top_level_entries(group, framework)
            prepared_entries = list()
            for _, entry in entries.iterrows():
                prepared_entries.append(prepare_entry(entry))
            framework_entries[framework] = prepared_entries
        top_level_entries[group] = framework_entries

    return top_level_entries


def list_sub_entries(data: dict):
    entries = find_sub_entries(data["group"], data["framework"], data["uri"])
    sub_entries = list()

    for _, entry in entries.iterrows():
        sub_entries.append(prepare_entry(entry))

    return sub_entries
