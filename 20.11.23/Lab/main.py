'''
Завдання 4
Створіть клас для представлення користувача з
атрибутами: ім'я та вік. Додайте властивості для
валідації віку користувача. Наприклад, вік повинен
бути у межах від 0 до 120
'''
from dataclasses import dataclass


class AgeDescriptor:
    age = 0

    def __set__(self, instance, value):
        if 0 < value < 120:
            self.age = value
        else:
            print('Age value not allowed. It should be more then 0 and less then 120!')

    def __get__(self, instance, owner):
        return self.age


@dataclass
class User:
    name: str
    age = AgeDescriptor()


user = User('Legolas')
user.age = 20
print(user.name)
print(user.age)
user.age = 50
print(user.name)
print(user.age)
user.age = 125
print(user.name)
print(user.age)
