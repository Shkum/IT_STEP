# Завдання 3
# Модифікуйте перше завдання так, щоб користувач не
# міг вводити запит, а користувався готовими фільтрами.
# Наприклад: відображення усіх людей, відображення усіх
# людей з одного міста (користувач задає з клавіатури як значення),
# відображення усіх людей з однієї країни (користувач задає з
# клавіатури як параметр).


from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import text
import json

with open('config.json') as f:
    data = dict(json.load(f))

user = data['user']
password = data['password']
db = 'people'
db_url = f"postgresql+psycopg2://{user}:{password}@localhost/{db}"
engine = create_engine(db_url)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    city = Column(String(50))
    country = Column(String(50))
    birthday = Column(Date)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# person1 = Person(first_name='John', last_name='Doe', city='New York', country='USA', birthday='1990-01-15')
# person2 = Person(first_name='Jane', last_name='Smith', city='London', country='UK', birthday='1985-03-22')
#
# session.add_all([person1, person2])
#
# session.commit()

filters = {'1': 'SELECT * FROM people', '2': 'SELECT first_name FROM people',
           '3': 'SELECT first_name, last_name from people', '4': "SELECT * FROM people WHERE city='London'"}

msg = '''
1 - Show table
2 - Show people`s names
3 - Show full names
4 - Show people from London
5 - Delete string with ID:...
6 - exit
    ----- > '''

while True:
    user_query = input(msg)
    if user_query in list('1234'):
        user_query = filters[user_query]
    elif user_query == '5':
        ids = input('Enter ID to delete: ')
        if not ids.isnumeric():
            print('ID must be a number')
            continue
        user_query = f'DELETE FROM people WHERE id = {ids}'
        result = session.execute(text(user_query))
        session.commit()
        print(f"\nID '{ids}' successfully deleted")
        continue
    else:
        print('Exiting...')
        break

    result = session.execute(text(user_query))
    rows = result.fetchall()
    if rows:
        print("Результат: ")
        for row in rows:
            print(*row)

session.close()
