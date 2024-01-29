# #
# Завдання
# Для бази даних Академія, яку ви розробили в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії
# з базою даних, який дозволяє:
# ■ вставляти рядки в таблиці бази даних;
# ■ оновлювати рядків у таблицях бази даних;
# ■ видаляти рядки з таблиць бази даних;
# ■ створювати звіти:
# ▷ вивести інформацію про всі навчальні групи,
# ▷ вивести інформацію про всіх викладачів,
# ▷ вивести назви усіх кафедр,
# ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі,
# ▷ вивести назви кафедр і груп, які до них відносяться,
# ▷ відобразити кафедру з максимальною кількістю груп,
# ▷ відобразити кафедру з мінімальною кількістю груп,
# ▷ вивести назви предметів, які викладає конкретний викладач,
# ▷ вивести назви кафедр, на яких викладається конкретна дисципліна,
# ▷ вивести назви груп, що належать до конкретного факультету,
# ▷ вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них,
# ▷ вивести назву предмету, за яким читається найменше лекцій,
# ▷ вивести назву предмету, за яким читається найбільше лекцій;
# ■ передбачити можливість збереження звітів з результатів роботи на екран або у файл (встановлюється в
# налаштуваннях додатку);
# ■ передбачити можливість входу з різними рівнями доступу. Наприклад: доступ лише для читання, доступ
# для читання та запис, доступ для читання певних таблиць.


from sqlalchemy import create_engine, MetaData, insert, Table, update, delete, select, join, func
import json

with open('config.json') as f:
    data = dict(json.load(f))

#                         VARIABLES
user = data['user']
password = data['password']
file_name = data['save_file']
access = data['access_level']
db = 'academy'

db_url = f"postgresql+psycopg2://{user}:{password}@localhost/{db}"
engine = create_engine(db_url)

savetofile = False  # change to True to save output to file as well

conn = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)


# або одна табличка
# departments = Table('departments', metadata, autoload=True, autoload_with=engine)

def print_table(table_name):
    table = Table(table_name, metadata, autoload=True)
    select_query = table.select()  # Исправлено здесь
    result = conn.execute(select_query)
    rows = result.fetchall()
    for row in rows:
        print(' '.join(map(lambda x: f'{str(x):20s}', row)))
        save_to_file(row)


def save_to_file(data):
    if savetofile:
        with open(file_name, 'a', encoding='utf8') as f:
            f.write('\n')
            f.write(data)


# ▷ вивести інформацію про всі навчальні групи
def all_groups():
    groups_table = Table('groups', metadata, autoload=True, autoload_with=engine)
    select_query = select(groups_table.c)
    with engine.connect() as conn:
        result = conn.execute(select_query)
        rows = result.fetchall()
    for row in rows:
        print(row)
        save_to_file(row)


# ▷ вивести інформацію про всіх викладачів
def all_teachers():
    groups_table = Table('teachers', metadata, autoload=True, autoload_with=engine)
    select_query = select(groups_table.c)
    with engine.connect() as conn:
        result = conn.execute(select_query)
        rows = result.fetchall()
    for row in rows:
        print(row)
        save_to_file(row)


# ▷ вивести назви усіх кафедр
def all_faculties():
    groups_table = Table('faculties', metadata, autoload=True, autoload_with=engine)
    select_query = select(groups_table.c)
    with engine.connect() as conn:
        result = conn.execute(select_query)
        rows = result.fetchall()
    for row in rows:
        print(row)
        save_to_file(row)


# ▷ вивести імена та прізвища викладачів, які читають лекції в конкретній групі
def lecturers_in_group(group_name='Group1'):
    curators_table = metadata.tables['curators']
    groups_curators_table = metadata.tables['groupscurators']
    groups_table = metadata.tables['groups']
    query = (
        select([curators_table.c.Name, curators_table.c.Surname])
        .select_from(
            join(groups_curators_table, curators_table, groups_curators_table.c.CuratorId == curators_table.c.Id))
        .select_from(join(groups_curators_table, groups_table, groups_curators_table.c.GroupId == groups_table.c.Id))
        .where(groups_table.c.Name == group_name)
    )

    with engine.connect() as conn:
        result = conn.execute(query)
        lecturers = result.fetchall()
    for lecturer in lecturers:
        print(f"{lecturer[0]} {lecturer[1]}")
        save_to_file(f"{lecturer[0]} {lecturer[1]}")


# ▷ вивести назви кафедр і груп, які до них відносяться
def departments_and_groups():
    departments_table = metadata.tables['departments']
    groups_table = metadata.tables['groups']
    query = (
        select([departments_table.c.Name, groups_table.c.Name])
        .select_from(join(departments_table, groups_table, departments_table.c.Id == groups_table.c.DepartmentId))
    )
    with engine.connect() as conn:
        result = conn.execute(query)
        data = result.fetchall()
    for department, group in data:
        print(f"Department: {department}, Group: {group}")
        save_to_file(f"Department: {department}, Group: {group}")


# ▷ відобразити кафедру з максимальною кількістю груп,
def department_with_max_groups():
    departments_table = metadata.tables['departments']
    groups_table = metadata.tables['groups']
    subquery = (
        select([groups_table.c.DepartmentId, func.count()])
        .group_by(groups_table.c.DepartmentId)
        .alias('group_counts')
    )
    query = (
        select([departments_table.c.Name])
        .select_from(departments_table.join(subquery, departments_table.c.Id == subquery.c.DepartmentId))
        .order_by(subquery.c.count.desc())
        .limit(1)
    )
    with engine.connect() as conn:
        result = conn.execute(query)
        data = result.fetchone()

    if data:
        print(f"Department with max groups: {data[0]}")
        save_to_file(f"Department with max groups: {data[0]}")
    else:
        print("No any department in DB")


# ▷ відобразити кафедру з мінімальною кількістю груп
def department_with_min_groups():
    departments_table = metadata.tables['departments']
    groups_table = metadata.tables['groups']
    subquery = (
        select([groups_table.c.DepartmentId, func.count()])
        .group_by(groups_table.c.DepartmentId)
        .alias('group_counts')
    )
    query = (
        select([departments_table.c.Name])
        .select_from(departments_table.join(subquery, departments_table.c.Id == subquery.c.DepartmentId))
        .order_by(subquery.c.count)
        .limit(1)
    )
    with engine.connect() as conn:
        result = conn.execute(query)
        data = result.fetchone()

    if data:
        print(f"Department with max groups: {data[0]}")
        save_to_file(f"Department with max groups: {data[0]}")
    else:
        print("No any department in DB")


# ▷ вивести назви предметів, які викладає конкретний викладач,
def subjects_taught_by_teacher(first_name='John', last_name='Doe'):
    teachers_table = metadata.tables['teachers']
    subjects_table = metadata.tables['subjects']
    subject_teacher_table = metadata.tables['subject_teacher']
    teacher_id_query = select([teachers_table.c.Id]).where(
        (teachers_table.c.Name == first_name) & (teachers_table.c.Surname == last_name)
    )
    with engine.connect() as conn:
        teacher_id_result = conn.execute(teacher_id_query)
        teacher_id = teacher_id_result.scalar()
    subjects_query = (
        select([subjects_table.c.Name])
        .select_from(
            join(subject_teacher_table, subjects_table, subject_teacher_table.c.SubjectId == subjects_table.c.Id)
        )
        .where(subject_teacher_table.c.TeacherId == teacher_id)
    )
    with engine.connect() as conn:
        subjects_result = conn.execute(subjects_query)
        subjects_taught = subjects_result.fetchall()
    if subjects_taught:
        print(f"Subjects of teacher {first_name} {last_name}: ")
        for subject in subjects_taught:
            print(subject[0])
            save_to_file(subject[0])
    else:
        print(f"Teacher {first_name} {last_name} has no any subject")
        save_to_file(f"Teacher {first_name} {last_name} has no any subject")


# ▷ вивести назви кафедр, на яких викладається конкретна дисципліна
def departments_teaching_subject(subject_name='Mathematics'):
    departments_table = metadata.tables['departments']
    subjects_table = metadata.tables['subjects']
    department_subject_table = metadata.tables['department_subject']
    departments_query = (
        select([departments_table.c.Name])
        .select_from(
            join(department_subject_table, departments_table,
                 department_subject_table.c.DepartmentId == departments_table.c.Id)
            .join(subjects_table, department_subject_table.c.SubjectId == subjects_table.c.Id)
        )
        .where(subjects_table.c.Name == subject_name)
    )
    with engine.connect() as conn:
        departments_result = conn.execute(departments_query)
        departments_teaching = departments_result.fetchall()
    if departments_teaching:
        print(f"Department name where '{subject_name}' available: ")
        for department in departments_teaching:
            print(department[0])
            save_to_file(department[0])
    else:
        print(f"Subject '{subject_name}' not available at any department")
        save_to_file(f"Subject '{subject_name}' not available at any department")


# ▷ вивести назви груп, що належать до конкретного факультету,
def groups_in_faculty(faculty_name='Engineering'):
    departments_table = metadata.tables['departments']
    groups_table = metadata.tables['groups']
    faculties_table = metadata.tables['faculties']
    groups_query = (
        select([groups_table.c.Name])
        .select_from(
            join(departments_table, groups_table, departments_table.c.Id == groups_table.c.DepartmentId)
            .join(faculties_table, departments_table.c.FacultyId == faculties_table.c.Id)
        )
        .where(faculties_table.c.Name == faculty_name)
    )
    with engine.connect() as conn:
        groups_result = conn.execute(groups_query)
        groups_in_faculty = groups_result.fetchall()
    if groups_in_faculty:
        print(f"Faculty group`s names '{faculty_name}': ")
        for group in groups_in_faculty:
            print(group[0])
            save_to_file(print(group[0]))
    else:
        print(f"Faculty '{faculty_name}' don`t have any group")


# ▷ вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них
def lectures_per_instructor_per_subject():
    lectures_table = metadata.tables['lectures']
    subjects_table = metadata.tables['subjects']
    instructors_table = metadata.tables['instructors']
    lectures_query = (
        select([
            instructors_table.c.Name,
            instructors_table.c.Surname,
            subjects_table.c.Name,
            func.count().label('Total_Lectures')
        ])
        .select_from(
            join(lectures_table, subjects_table, lectures_table.c.SubjectId == subjects_table.c.Id)
            .join(instructors_table, lectures_table.c.InstructorId == instructors_table.c.Id)
        )
        .group_by(instructors_table.c.Name, instructors_table.c.Surname, subjects_table.c.Name)
        .order_by(func.count().desc())
    )
    with engine.connect() as conn:
        lectures_result = conn.execute(lectures_query)
        lectures_per_instructor_per_subject = lectures_result.fetchall()
    if lectures_per_instructor_per_subject:
        print("Max lecture quantity for each subject: ")
        for row in lectures_per_instructor_per_subject:
            instructor_name = f"{row[0]} {row[1]}"
            subject_name = row[2]
            total_lectures = row[3]
            print(f"{subject_name}: {instructor_name} - {total_lectures} lectures")
            save_to_file(f"{subject_name}: {instructor_name} - {total_lectures} lectures")
    else:
        print("No any record about lectures")


# ▷ вивести назву предмету, за яким читається найменше лекцій
def subject_with_least_lectures():
    lectures_table = metadata.tables['lectures']
    subjects_table = metadata.tables['subjects']
    lectures_query = (
        select([
            subjects_table.c.Name,
            func.count().label('Total_Lectures')
        ])
        .select_from(
            lectures_table.join(subjects_table, lectures_table.c.SubjectId == subjects_table.c.Id)
        )
        .group_by(subjects_table.c.Name)
        .order_by(func.count())
        .limit(1)
    )
    with engine.connect() as conn:
        lectures_result = conn.execute(lectures_query)
        subject_with_least_lectures = lectures_result.fetchone()
    if subject_with_least_lectures:
        subject_name = subject_with_least_lectures[0]
        total_lectures = subject_with_least_lectures[1]
        print(f"Subject with minimum lectures: {subject_name} - {total_lectures} lectures")
        save_to_file(f"Subject with minimum lectures: {subject_name} - {total_lectures} lectures")
    else:
        print("No any lectures in DB")


# ▷ вивести назву предмету, за яким читається найбільше лекцій
def subject_with_most_lectures():
    lectures_table = metadata.tables['lectures']
    subjects_table = metadata.tables['subjects']
    lectures_query = (
        select([
            subjects_table.c.Name,
            func.count().label('Total_Lectures')
        ])
        .select_from(
            lectures_table.join(subjects_table, lectures_table.c.SubjectId == subjects_table.c.Id)
        )
        .group_by(subjects_table.c.Name)
        .order_by(func.count().desc())
        .limit(1)
    )
    with engine.connect() as conn:
        lectures_result = conn.execute(lectures_query)
        subject_with_most_lectures = lectures_result.fetchone()
    if subject_with_most_lectures:
        subject_name = subject_with_most_lectures[0]
        total_lectures = subject_with_most_lectures[1]
        print(f"Subject with max lectures: {subject_name} - {total_lectures} lectures")
        save_to_file(f"Subject with max lectures: {subject_name} - {total_lectures} lectures")
    else:
        print("No any lectures in DB")


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


menu = '''
MENU:
1 - Add row
2 - Update row
3 - Delete row
0 - Exit

Enter your selection: '''

while True:
    if access == 'admin':
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
    else:
        print('You dont have ADMIN privilege.\nYour allowed only to read DB')
        break

funcs = [
    all_groups,
    all_teachers,
    all_faculties,
    lecturers_in_group,
    departments_and_groups,
    department_with_max_groups,
    department_with_min_groups,
    subjects_taught_by_teacher,
    departments_teaching_subject,
    groups_in_faculty,
    lectures_per_instructor_per_subject,
    subject_with_least_lectures,
    subject_with_most_lectures
]


for func in funcs:
    try:
        func()
    except BaseException as er:
        print(f'"{func.__name__}" Error: {er}')
        continue
