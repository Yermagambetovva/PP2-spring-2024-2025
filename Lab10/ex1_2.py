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
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    print("Данные из CSV загружены.")

def insert_from_console():
    config = load_config()
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Данные добавлены.")

def update_data():
    config = load_config()
    old_name = input("Введите имя, которое хотите обновить: ")
    new_name = input("Новое имя: ")
    new_phone = input("Новый номер телефона: ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET name=%s, phone=%s WHERE name=%s", (new_name, new_phone, old_name))
    print("Данные обновлены.")

def query_data():
    config = load_config()
    filter_name = input("Фильтр по имени (Enter — пропустить): ")
    filter_phone = input("Фильтр по телефону (Enter — пропустить): ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if filter_name and filter_phone:
                cur.execute("SELECT * FROM phonebook WHERE name=%s AND phone=%s", (filter_name, filter_phone))
            elif filter_name:
                cur.execute("SELECT * FROM phonebook WHERE name=%s", (filter_name,))
            elif filter_phone:
                cur.execute("SELECT * FROM phonebook WHERE phone=%s", (filter_phone,))
            else:
                cur.execute("SELECT * FROM phonebook")
            for row in cur.fetchall():
                print(row)

def delete_data():
    config = load_config()
    name = input("Имя для удаления: ")
    phone = input("Телефон для удаления: ")
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE name=%s AND phone=%s", (name, phone))
    print("Данные удалены.")
