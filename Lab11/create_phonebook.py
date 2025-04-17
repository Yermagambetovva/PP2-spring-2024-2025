import psycopg2
from config import load_config

def create_tables():
    """Create the correct phonebook1 table in PostgreSQL"""
    command = """
    CREATE TABLE IF NOT EXISTS phonebook1 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("Таблица phonebook успешно создана.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при создании таблицы:", error)

if __name__ == '__main__':
    create_tables()
