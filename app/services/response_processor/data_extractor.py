import json


def extract_data(raw_data: str):
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
