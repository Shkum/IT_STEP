'''
Завдання 5
Створіть клас Character, який має атрибути name, health
та damage. Реалізуйте метод класу attack, який виводить
повідомлення про атаку гравця.
'''
from dataclasses import dataclass


@dataclass
class Character:
    name: str
    health: int
    damage: int


    @classmethod
    def attack(cls, char):
        return f'Character "{char.name}", with health "{char.health}", is attacking now with attack power "{char.damage}"'


char = Character('Mr. Bin', 120, 30)
print(char)
print(Character.attack(char))

