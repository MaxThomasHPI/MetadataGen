import psycopg
import os


def connect_to_database():
    return psycopg.connect(
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host="127.0.0.1",
        port="5432"
    )
