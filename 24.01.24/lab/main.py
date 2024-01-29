# Завдання 2
# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії
# з базою даних, який дозволяє створювати звіти:
# ▷ Вивести прізвища лікарів та їх спеціалізації;
# ▷ Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці;
# ▷ Вивести назви палат, які знаходяться у певному відділенні;
# ▷ Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;
# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією

from sqlalchemy import create_engine, MetaData, Table, select, func, join
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


def print_table(table_name):
    table = Table(table_name, metadata, autoload=True)
    select_query = table.select()  # Исправлено здесь
    result = conn.execute(select_query)
    rows = result.fetchall()
    for row in rows:
        print(' '.join(map(lambda x: f'{str(x):20s}', row)))


def print_all_tables():
    for table_name in metadata.tables.keys():
        print(table_name)


# ▷ Вивести прізвища лікарів та їх спеціалізації
def doctors_specialization():
    doctors = metadata.tables['doctors']
    specializations = metadata.tables['specializations']
    doctors_specializations = metadata.tables['doctors_specializations']

    query = select(
        doctors.c.surname,
        specializations.c.name
    ).select_from(
        doctors.join(doctors_specializations, doctors.c.id == doctors_specializations.c.doctor_id)
        .join(specializations, specializations.c.id == doctors_specializations.c.specialization_id)
    )

    result = conn.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(*row)


# ▷ Вивести прізвища та зарплати (сума ставки та надбавки)
def doctors_salary():
    doctors = metadata.tables['doctors']
    query = select(
        doctors.c.surname,
        doctors.c.salary + doctors.c.premium
    )

    result = conn.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(*row)


# ▷ Вивести назви палат, які знаходяться у певному відділенні;
def wards_in_department(department_name):
    wards = metadata.tables['wards']
    departments = metadata.tables['departments']

    query = select(
        wards.c.name
    ).select_from(
        wards.join(departments, wards.c.department_id == departments.c.id)
    ).where(departments.c.name == department_name)

    result = conn.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(row[0])


# Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;
def donations_by_month(month):
    donations = metadata.tables['donations']
    departments = metadata.tables['departments']
    sponsors = metadata.tables['sponsors']

    query = select(
        departments.c.name.label('department'),
        sponsors.c.name.label('sponsor'),
        func.sum(donations.c.amount).label('total_amount'),
        donations.c.date
    ).select_from(
        donations.join(departments, donations.c.department_id == departments.c.id)
        .join(sponsors, donations.c.sponsor_id == sponsors.c.id)
    ).where(
        func.extract('month', donations.c.date) == month
    ).group_by(
        departments.c.name,
        sponsors.c.name,
        donations.c.date
    )

    result = conn.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(row[0])


# ▷ Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;
def sponsored_departments_by_company(company_name):
    departments = metadata.tables['departments']
    sponsors = metadata.tables['sponsors']
    donations = metadata.tables['donations']

    query = (select(departments.c.name.distinct()).
             select_from(join(departments, join(donations, donations.c.department_id == departments.c.id),
                              donations.c.sponsor_id == sponsors.c.id)).where(sponsors.c.name == company_name))

    result = conn.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(row[0])


# doctors_specialization()
# doctors_salary()
# wards_in_department('Department A')
donations_by_month(1)
