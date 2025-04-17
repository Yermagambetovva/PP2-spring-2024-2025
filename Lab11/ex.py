import psycopg2
import csv
from connect import connect

def upload_from_csv(path='data.csv'):
    conn = connect()
    cur = conn.cursor()
    with open(path, 'r') as file:
        reader = csv.reader(file)
        names, phones = [], []
        for row in reader:
            names.append(row[0])
            phones.append(row[1])
    cur.execute("CALL insert_many_users(%s, %s, NULL)", (names, phones))
    conn.commit()
    conn.close()

def manual_insert():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(CAST(%s AS TEXT), CAST(%s AS TEXT))", (name, phone))
    conn.commit()
    conn.close()

def search_by_pattern():
    pattern = input("Enter pattern: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)
    conn.close()

def paginate():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)
    conn.close()

def delete_user():
    value = input("Enter name or phone to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(CAST(%s AS TEXT))", (value,))
    conn.commit()
    conn.close()

def menu():
    while True:
        print("\nPhoneBook Menu")
        print("1 - Upload from CSV")
        print("2 - Manual Insert")
        print("3 - Search by Pattern")
        print("4 - Paginated Users")
        print("5 - Delete User")
        print("0 - Exit")

        choice = input("Choose option: ")
        if choice == '1':
            upload_from_csv()
        elif choice == '2':
            manual_insert()
        elif choice == '3':
            search_by_pattern()
        elif choice == '4':
            paginate()
        elif choice == '5':
            delete_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
