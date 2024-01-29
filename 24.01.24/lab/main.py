# Завдання 3
# Для бази даних «Лікарня», яку ви створювали в рамках
# курсу «Теорія баз даних», реалізуйте програму, яка дозволить
# працювати зі структурою бази даних. Програма має:
# ■ відображати назви усіх таблиць;
# ■ відображати назви стовпців певної таблиці;
# ■ відображати назви стовпців та їх типи для певної таблиці;
# ■ відображати зв’язки між таблицями;
# ■ вміти створювати таблиці;
# ■ видаляти таблиці;
# ■ додавати стовпці;
# ■ оновлювати стовпці;
# ■ видаляти стовпці.

from sqlalchemy import create_engine, MetaData, Table, select, func, join, Column, Integer, String, delete,insert, update
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


def print_all_tables():
    print('       TABLES NAMES')
    for table_name in metadata.tables.keys():
        print(table_name)


def print_columns(table_name):
    table = metadata.tables[table_name]
    print("\n       COLUMNS NAMES:")
    for column in table.columns:
        print(column.name)


def print_columns_types(table_name):
    table = metadata.tables[table_name]
    print("\nCOLUMN NAMES AND TYPES:")
    for column in table.c:
        print(f"{column.name}: {column.type}")


def print_relationships(table_name):
    foreign_keys = metadata.tables[table_name].foreign_keys
    print("\nFOREIGN KEYS AND RELATIONS:")
    for fk in foreign_keys:
        print(
            f"Table '{fk.parent.table.name}' column '{fk.parent.name}' references table '{fk.column.table.name}' column '{fk.column.name}'")


def create_table(table_name, columns):
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)
    print(f"Table '{table_name}' has been created.")


def drop_table(table_name):
    if table_name in metadata.tables:
        metadata.tables[table_name].drop(engine)
        print(f"Table '{table_name}' has been dropped.")
    else:
        print(f"Table '{table_name}' does not exist.")


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
    else:
        print("Delete canceled!")



print_all_tables()
print_columns('doctors')
print_columns_types('doctors')
print_relationships('wards')

columns = [
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
]
create_table('test', columns)

drop_table('test')
add_row('doctors')
update_rows('doctors')
delete_rows('doctors')

