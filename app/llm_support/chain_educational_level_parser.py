def parse_educational_level_input(input_data):
    input_data = input_data.get("educationalLevel", "DigComp")

    if type(input_data) == str:
        return input_data

    return input_data[0]["educationalFramework"]
