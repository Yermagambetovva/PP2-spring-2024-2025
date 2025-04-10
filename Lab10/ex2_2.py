import psycopg2
from config import load_config

def create_table():
    command = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            level INTEGER NOT NULL,
            score INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command)
    print("Таблица users создана.")

def insert_user(username, level, score):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (username, level, score)
                VALUES (%s, %s, %s)
            """, (username, level, score))
    print("Данные сохранены.")

def get_last_level(username):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT MAX(level) FROM users WHERE username = %s
            """, (username,))
            level = cur.fetchone()[0]
            return level if level else 1

def get_user_score(username):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username = %s ORDER BY timestamp DESC", (username,))
            for row in cur.fetchall():
                print(row)
