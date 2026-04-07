from app.suggestion_logging.table_checker import check_table
from app.suggestion_logging.database_connector import connect_to_database
import json


def write_log(generated_metadata):
    check_table()

    conn = connect_to_database()
    cursor = conn.cursor()

    attributes = [
        "name",
        "description",
        "educationalAlignment",
        "teaches",
        "keywords",
        "educationalLevel"
    ]

    data = list()

    for attribute in attributes:
        datum = generated_metadata.get(attribute, None)
        data.append(json.dumps(datum))

    statement = f"""
        INSERT INTO suggestion_log (name, description, educationalAlignment, 
        teaches, keywords, educationalLevel) VALUES (%s, %s, %s, %s, %s, %s);
    """

    cursor.execute(statement, data)
    conn.commit()

    cursor.close()
    conn.close()
