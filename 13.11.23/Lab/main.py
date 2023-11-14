'''Завдання 3
Створіть базовий клас «Тварина» та похідні класи:
«Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
конструктора ім’я кожної тварини та її характеристики.
Створіть для кожного класу необхідні методи та поля.'''
from dataclasses import dataclass


@dataclass
class Animal:
    _name: str
    _sound: str
    _type: str

    def make_sound(self):
        print(f'{self._type} {self._name} saying {self._sound}')

    def move(self):
        print(f'{self._type} {self._name} moving')

    def swim(self, can_swim: bool):
        print(f"{self._type} {self._name} {'can swim' if can_swim else 'can not swim'}")


@dataclass
class Tiger(Animal):

    def swim(self, can_swim=True):
        super().swim(can_swim)


@dataclass
class Crocodile(Animal):

    def swim(self, can_swim=True):
        super().swim(can_swim)


@dataclass
class Gorilla(Animal):

    def swim(self, can_swim=False):
        super().swim(can_swim)


tiger = Tiger('Sherhan', 'Grrrrr', 'Tiger')
tiger.swim()
tiger.move()
print('=' * 30)
croco = Crocodile('Gena', 'Breee', 'Crocodile')
croco.swim()
croco.move()
print('=' * 30)
gorilla = Gorilla('Abu', 'Uuuu-Aaaa', 'Monkey')
gorilla.swim()
gorilla.move()
