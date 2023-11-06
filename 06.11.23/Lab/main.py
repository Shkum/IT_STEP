'''
Завдання 1
Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
"email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
дані можна отримати лише через методи класу.
'''
from dataclasses import dataclass


@dataclass
class User:

    '''Create and manage user object'''

    _name: str
    _age: int
    _email: str

    def __str__(self):
        return f'{self._name} - {self._age} - {self._email}'

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email


user = User('Petro', 20, 'da@da.da')
print(user)
print(user.get_name())
user.set_name('Ivane')
print(user)
print(user.get_name())
print(user.__repr__())
print(user.__doc__)


