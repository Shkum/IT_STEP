# Завдання 4
# Модифікуйте третє завдання, щоб фільтр для показу міг бути комплексним. Наприклад, користувач може
# виставити фільтр на країну та місто, після чого відобразяться люди, для яких спрацює цей комплексний
# фільтр. Підтримайте умову АБО
import sqlalchemy.exc
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
           '3': 'SELECT first_name, last_name from people',
           '4': "SELECT * FROM people WHERE city='London'"}

msg = '''
1 - Show table
2 - Show people`s names
3 - Show full names
4 - Show people from London
5 - Delete string with ID:...
6 - Create your own filter
7 - Exit
    ----- > '''

own_filter = {'1': 'id', '2': 'first_name', '3': 'last_name', '4': 'city', '5': 'country', '6': 'birthday'}


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

    elif user_query == '6':
        custom_filter = {}
        while True:
            print('\n>>>List of filters<<<')
            for i, v in own_filter.items():
                print(f'{i} - {v}')
            filt = input('Select filter number (0 - stop customization): ')
            if filt in own_filter:
                value = input('Enter value for filter: ')
                custom_filter[own_filter[filt]] = f"'{value}'" if filt != '1' else int(value)
            else:
                print('\nCustomization of filter completed\n')
                break
            query_condition = []
            for i, v in custom_filter.items():
                query_condition.append(f'{i}={v}')
            query_condition = 'WHERE ' + ' AND '.join(query_condition)
            user_query = f'SELECT * FROM people {query_condition}'

            print(user_query)


    else:
        print('Exiting...')
        break
    try:
        result = session.execute(text(user_query))
        rows = result.fetchall()
        if rows:
            print("\nResult: ")
            for row in rows:
                print(*row)
    except sqlalchemy.exc.ProgrammingError as er:
        print('Error', er)

session.close()