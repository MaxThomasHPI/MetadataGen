import psycopg
from app.suggestion_logging.database_connector import connect_to_database


def check_table():
    conn = connect_to_database()
    courser = conn.courser()
    statement = """
        CREATE TABEL IF NOT EXISTS suggestion_log(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            edalign TEXT,
            teaches TEXT,
            keywords TEXT,
            edlevel TEXT,
            date TIMESTAMPTZ
        )
        """
    conn.close()
