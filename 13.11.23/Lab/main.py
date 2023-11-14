'''Завдання 1
Створіть клас Human, який міститиме інформацію
про людину.
За допомогою механізму успадкування реалізуйте
клас Builder (містить інформацію про будівельника),
клас Sailor (містить інформацію про моряка), клас Pilot
(містить інформацію про льотчика).
Кожен із класів має містити необхідні для роботи
методи'''
from dataclasses import dataclass


@dataclass
class Human:
    _name: str
    _family_name: str
    _age: int
    _address: str

    def __init__(self):
        self._ability = None

    def change_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def change_family_name(self, family_name):
        self._family_name = family_name

    def get_family_name(self):
        return self._family_name

    def change_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def change_address(self, address):
        self._address = address

    def get_address(self):
        return self._address

    def get_info(self):
        print(f'Ability for {self.__class__.__name__} {self._name}: {self._ability}' )


@dataclass
class Builder(Human):
    _ability = 'can build'

    def make_action(self):
        print(f'{self._name} {self._ability}')


@dataclass
class Sailor(Human):
    _ability = 'can sail'

    def make_action(self):
        print(f'{self._name} {self._ability}')


@dataclass
class Pilot(Human):
    _ability = 'can fly'

    def make_action(self):
        print(f'{self._name} {self._ability}')


person1 = Builder('Tom', 'Jerry', 30, 'Earth')
person1.get_info()
person1.make_action()

print()

person2 = Sailor('Jerry', 'Tom', 25, 'Europe')
person2.get_info()
person2.make_action()

print()

person3 = Pilot('Ninja', 'Turtle', 35, 'Usa')
person3.get_info()
person3.make_action()
