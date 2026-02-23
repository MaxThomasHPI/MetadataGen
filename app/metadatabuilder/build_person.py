def build_all_persons_fragments(persons: list) -> list:
    """
    Creates a list containing all Person metadata fragments based on a given list of raw person data.

    :param persons: A list with dictionaries containing the raw Person objects to be converted into the MOOChub format.
    :type persons: list
    :return: A list with MOOChub conform Person objects.
    :rtype: list
    """

    return [build_person_fragment(person) for person in persons]


def build_person_fragment(person_data: dict) -> dict:
    """
    Adds the mandatory "type" attribute to the person metadata fragment and sets it to "Person".

    :param person_data: A raw Person object.
    :type person_data: dict
    :return: A Organization object with the minimal requirements to conform with the MOOChub format.
    :rtype: dict
    """
    person_data["type"] = "Person"

    return person_data
