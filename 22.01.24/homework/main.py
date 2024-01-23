# Завдання 1
# Створіть тритабличну базу даних Sales (Продажі). У цій
# базі даних мають бути таблиці: Sales (інформація про конкретні
# продажі), Salesmen (інформація про продавців), Customers (інформація про покупців).
# Створіть додаток для відображення
# даних з таблиць. Меню додатку має містити такий мінімальний набір звітів:
# ■ Відображення усіх угод;
# ■ Відображення угод конкретного продавця;
# ■ Відображення максимальної за сумою угоди;
# ■ Відображення мінімальної за сумою угоди;
# ■ Відображення максимальної суми угоди для конкретного продавця;
# ■ Відображення мінімальної за сумою угоди для конкретного продавця;
# ■ Відображення максимальної за сумою угоди для конкретного покупця;
# ■ Відображення мінімальної за сумою угоди для конкретного покупця;
# ■ Відображення продавця з максимальною сумою продажів за всіма угодами;
# ■ Відображення продавця з мінімальною сумою продажів за всіма угодами;
# ■ Відображення покупця з максимальною сумою покупок за всіма угодами;
# ■ Відображення середньої суми покупки для конкретного покупця;
# ■ Відображення середньої суми покупки для конкретного продавця.

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker, declarative_base
import json

with open('config.json') as f:
    data = dict(json.load(f))

#                                         VARIABLES
user = data['user']
password = data['password']
file_name = data['save_file']
db = 'sales'
db_url = f"postgresql+psycopg2://{user}:{password}@localhost/{db}"
engine = create_engine(db_url)
Base = declarative_base()


#                                      CREATE TABLES
class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, Sequence('sales_id_seq'), primary_key=True)
    date = Column(Date)
    amount = Column(Integer)
    salesman_id = Column(Integer, sqlalchemy.ForeignKey('salesmen.id'))
    customer_id = Column(Integer, sqlalchemy.ForeignKey('customers.id'))

    def __str__(self):
        return f"ID: {self.id}, Salesman ID: {self.salesman_id}, Customer ID: {self.customer_id}, Amount: {self.amount}"


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, Sequence('salesmen_id_seq'), primary_key=True)
    name = Column(String(50))
    sales = sqlalchemy.orm.relationship('Sales', backref='salesman')


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, Sequence('customers_id_seq'), primary_key=True)
    name = Column(String(50))
    sales = sqlalchemy.orm.relationship('Sales', backref='customer')


Base.metadata.create_all(engine)

#                                            FILL UP TABLES
from datetime import date

Session = sessionmaker(bind=engine)
session = Session()

for i in range(1, 11):
    salesman = Salesmen(name=f'Salesman {i}')
    session.add(salesman)

for i in range(1, 11):
    customer = Customers(name=f'Customer {i}')
    session.add(customer)

for i in range(1, 11):
    sale = Sales(
        date=date.today(),
        amount=i * 100,
        salesman_id=i,
        customer_id=i
    )
    session.add(sale)

session.commit()


# Відображення усіх угод
def display_all_sales(session):
    sales = session.query(Sales).all()
    print("\nУсі угоди:")
    for sale in sales:
        print(sale)


# Відображення угод конкретного продавця
def display_sales_by_salesman(session, salesman_id):
    sales = session.query(Sales).filter_by(salesman_id=salesman_id).all()
    print(f"\nУгоди продавця з id {salesman_id}:")
    for sale in sales:
        print(sale)


# Відображення максимальної за сумою угоди
def display_max_sale(session):
    max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
    print(f"\nМаксимальна за сумою угода:")
    print(max_sale)


# Відображення мінімальної за сумою угоди
def display_min_sale(session):
    min_sale = session.query(Sales).order_by(Sales.amount).first()
    print(f"\nМінімальна за сумою угода:")
    print(min_sale)


# Відображення максимальної суми угоди для конкретного продавця
def display_max_sale_by_salesman(session, salesman_id):
    max_sale = session.query(Sales).filter_by(salesman_id=salesman_id).order_by(Sales.amount.desc()).first()
    print(f"\nМаксимальна за сумою угода для продавця з id {salesman_id}:")
    print(max_sale)


with Session() as session:
    display_all_sales(session)
    display_sales_by_salesman(session, 1)
    display_max_sale(session)
    display_min_sale(session)
    display_max_sale_by_salesman(session, 1)
