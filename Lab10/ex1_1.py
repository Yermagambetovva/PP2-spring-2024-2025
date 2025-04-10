import psycopg2
from config import load_config

def create_tables():
    """Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,          
            name VARCHAR(255) NOT NULL,     
            phone VARCHAR(20) NOT NULL      
        )
        """,

    )
    try:
        config = load_config()              #загружаем параметры подключения из config файла
        with psycopg2.connect(**config) as conn:   #устанавливаем соединение с базой
            with conn.cursor() as cur:             #открываем курсор для выполнения SQL-команд
                for command in commands:
                    cur.execute(command)           #выполняем SQL-команду
                print("Таблица успешно создана.")  #подтверждение успешного создания
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при создании таблицы:", error)  #обработка ошибок

if __name__ == '__main__':
    create_tables()  #запуск функции при выполнении скрипта напрямую
