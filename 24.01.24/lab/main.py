# Завдання 1
# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії з базою даних, який дозволяє:
# ■ Вставляти рядки в таблиці бази даних.
# ■ Оновлення рядків у таблицях бази даних. При спробі оновлення усіх рядків в одній
# таблиці надайте запит на підтвердження користувачеві. Оновлювати усі рядки можна
# лише після підтвердження користувачем.
# ■ Видалення рядків з таблиць баз даних. При спробі видалити усі рядки в одній
# таблиці потрібно видавати користувачу запит на підтвердження. Видаляти усі рядки,
# можна тільки після підтвердження користувачем

from sqlalchemy import create_engine, MetaData, insert, Table, update, delete, select, join, func
import json

with open('config.json') as f:
    data = dict(json.load(f))

#                                                   VARIABLES
user = data['user']
password = data['password']
file_name = data['save_file']
db = 'hospital'

db_url = f"postgresql+psycopg2://{user}:{password}@localhost/{db}"
engine = create_engine(db_url)

conn = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)


#                                                   METHODS
def print_table(table_name):
    table = Table(table_name, metadata, autoload=True)
    select_query = table.select()
    result = conn.execute(select_query)
    rows = result.fetchall()
    for row in rows:
        print(' '.join(map(lambda x: f'{str(x):20s}', row)))


def add_row(table):
    columns = table.columns.keys()
    values = {}
    for column in columns:
        value = input(f"Enter value for column '{column}': ")
        values[column] = value
    query = insert(table).values(values)
    conn.execute(query)
    conn.commit()
    print("\nRow appended!\n")
    print_table(table.name)


def update_rows(table):
    columns = table.columns.keys()
    print("Available columns: ")
    for idx, column in enumerate(columns, start=1):
        print(f"{idx}.{column}")
    selected_column_idx = int(input("Enter column number for searching: "))

    if 1 <= selected_column_idx <= len(columns):
        condition_column = columns[selected_column_idx - 1]
    else:
        print("Wrong column number!")

    condition_value = input(f"Enter value to find row in column '{condition_column}': ")
    new_values = {}
    for column in columns:
        value = input(f"Enter new value for column '{column}': ")
        new_values[column] = value

    confirm_update = input("Update row? y/n?: ")
    if confirm_update.lower() == 'y':
        query = update(table).where(getattr(table.c, condition_column) == condition_value).values(new_values)
        conn.execute(query)
        conn.commit()

        print("\nUpdate completed!\n")
        print_table(table.name)

    else:
        print("Update canceled!")


def delete_rows(table):
    columns = table.columns.keys()
    print("Available columns: ")
    for idx, column in enumerate(columns, start=1):
        print(f"{idx}.{column}")
    selected_column_idx = int(input("Enter column number for searching value for deleting: "))

    if 1 <= selected_column_idx <= len(columns):
        condition_column = columns[selected_column_idx - 1]
    else:
        print("Wrong column number")

    condition_value = input(f"Enter value to search in '{condition_column}': ")

    confirm_update = input("Delete rows with selected values?  y/n?: ")
    if confirm_update.lower() == 'y':
        query = delete(table).where(getattr(table.c, condition_column) == condition_value)
        conn.execute(query)
        conn.commit()

        print("Rows deleted!")
        print_table(table.name)
    else:
        print("Delete canceled!")


#                                             MENU LOOP
menu = '''
MENU:
1 - Add row
2 - Update row
3 - Delete row
0 - Exit

Enter your selection: '''

while True:
    print("\nList of tables: \n")
    for table_name in metadata.tables.keys():
        print(table_name)
    table_name = input("\nEnter table name or '0' to exit: ")
    if table_name == '0':
        break
    if table_name in metadata.tables:
        table = metadata.tables[table_name]
        print(f"\nSelected table: '{table_name}'\n")
        print_table(table_name)
        choice = input(menu)
        if choice == "1":
            add_row(table)
        elif choice == "2":
            update_rows(table)
        elif choice == "3":
            delete_rows(table)
        elif choice == "0":
            break
        else:
            print("Wrong data entered.")
    else:
        print("Table not found.")
