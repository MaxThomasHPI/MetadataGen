import psycopg
import os


def connect_to_database():
    return psycopg.connect(
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host="logging_suggestion_db",
        port="5432"
    )
