from app.helper.paths import FRAMEWORK_ROOT


def check_for_vector_dbs(conf: dict) -> tuple[list, dict]:
    """
    Checks if a vector database already exists for a framework. The method will
    iterate over all frameworks given in the config file. It returns a list of
    frameworks that still not embedded and stored in a vector DB together with
    the config file.

    :param conf: The config file that contains the framework names as keys and
    additional data (e.g. which embedding function to use).
    :type conf: dict
    :return: A list with the config file and the names of the frameworks missing a vector DB.
    :rtype: tuple[list, dict]
    """
    not_found = list()

    for k, v in conf.items():
        path = (
            FRAMEWORK_ROOT /
            v["GROUP"] /
            k /
            "chroma.sqlite3"
        )

        if not path.exists():
            not_found.append(k)

    return not_found, conf
