# Завдання 1
# Створіть однотабличну базу даних People (ім’я, прізвище, місто, країна, дата народження) з однойменною
# таблицею. Напишіть програму, яка дозволяє користувачеві ввести запит і отримати результати роботи запиту.
# Підтримуйте лише SELECT як запит. Якщо ви спробуєте
# виконати інші запити, потрібно буде генерувати помилку

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

print(engine)

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

while True:
    user_query = input("Enter your query (exit - exit): ")
    if user_query.lower() == "exit":
        break
    try:
        result = session.execute(text(user_query))
        session.commit()
        print("Successfully completed")
    except Exception as e:
        print(f"Query error: {e}")

session.close()
