import psycopg2
import csv
from config import load_config

def insert_from_csv(filename):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    cur.execute("INSERT INTO phonebooklab10 (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    print("Данные из CSV загружены.")

def insert_from_console():
    config = load_config()
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebooklab10 (name, phone) VALUES (%s, %s)", (name, phone))
    print("Данные добавлены.")

def update_data():
    config = load_config()
    old_name = input("Введите имя, которое хотите обновить: ")
    new_name = input("Новое имя: ")
    new_phone = input("Новый номер телефона: ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebooklab10 SET name=%s, phone=%s WHERE name=%s", (new_name, new_phone, old_name))
    print("Данные обновлены.")

def query_data():
    config = load_config()
    filter_name = input("Фильтр по имени (Enter — пропустить): ")
    filter_phone = input("Фильтр по телефону (Enter — пропустить): ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if filter_name and filter_phone:
                cur.execute("SELECT * FROM phonebooklab10 WHERE name=%s AND phone=%s", (filter_name, filter_phone))
            elif filter_name:
                cur.execute("SELECT * FROM phonebooklab10 WHERE name=%s", (filter_name,))
            elif filter_phone:
                cur.execute("SELECT * FROM phonebooklab10 WHERE phone=%s", (filter_phone,))
            else:
                cur.execute("SELECT * FROM phonebooklab10")
            for row in cur.fetchall():
                print(row)

def delete_data():
    config = load_config()
    name = input("Имя для удаления: ")
    phone = input("Телефон для удаления: ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebooklab10 WHERE name=%s AND phone=%s", (name, phone))
    print("Данные удалены.")


def menu():
    while True:
        print("\nМеню:")
        print("1 - Импорт из CSV")
        print("2 - Ввод с консоли")
        print("3 - Обновить запись")
        print("4 - Найти запись")
        print("5 - Удалить запись")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            insert_from_csv("data.csv")  # имя CSV-файла можно изменить
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '0':
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    menu()
