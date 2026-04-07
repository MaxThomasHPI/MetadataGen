from app.suggestion_logging.database_connector import connect_to_database


def check_table():
    conn = connect_to_database()
    cursor = conn.cursor()
    statement = """
        CREATE TABLE IF NOT EXISTS suggestion_log(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            description TEXT,
            educationalAlignment TEXT,
            teaches TEXT,
            keywords TEXT,
            educationalLevel TEXT
        );
        """
    cursor.execute(statement)
    conn.commit()

    cursor.close()
    conn.close()
