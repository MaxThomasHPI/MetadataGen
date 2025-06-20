"""
Extracts the data from the LLM response and parses it. The response has to be given in a defined format so it can be
processed.
"""


import json


def extract_data(raw_data: str) -> dict:
    """
    Extracts and parses the received data from the LLM. It converts it into a dictionary where the different attributes
    are the keys and the values are the suggested attribute values.

    :param raw_data: The raw data as a text directly received from the LLM.
    :type raw_data: str
    :return: The parsed metadata suggestion for the different attributes.
    :rtype: dict
    """
    lines = list()
    raw_data = raw_data.split('\n')

    for line in raw_data:
        if "=" in line:
            lines.append(line)

    data = dict()
    for line in lines:
        attribute, line = line.split(' = ')

        while "'" in line:
            line = line.replace("'", '"')

        try:
            line = json.loads(line)
        except json.decoder.JSONDecodeError:
            pass

        data[attribute] = line

    return data
