'''Завдання 6
Створіть клас Student, який має атрибути name, age,
grade та courses. Реалізуйте метод класу add_course, який
додає новий предмет до списку курсів студента'''
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    _grade: int
    _courses: list


    @classmethod
    def add_course(cls, student, course):
        student._courses.append(course)
        print('New course added...')


student = Student('Aragorn', 250, 5, ['magic', 'esoteric', 'dark magic'])
print(student)
print(student._courses)
student.add_course(student, 'necromancy')
print(student)
print(student._courses)

