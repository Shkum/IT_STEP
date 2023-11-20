'''
Завдання 5
Створіть клас Multiplier, який при ініціалізації
отримує множник. Забезпечте можливість викликати
цей об'єкт з аргументом та повертати множене
значення
'''
from dataclasses import dataclass


@dataclass
class Multiplier:
    first_multiplier: float

    def __call__(self, second_multiplier):
        return self.first_multiplier * second_multiplier


multiply = Multiplier(10)
print(multiply(5))
