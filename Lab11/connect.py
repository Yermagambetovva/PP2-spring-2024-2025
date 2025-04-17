import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="maradato2512"
    )
