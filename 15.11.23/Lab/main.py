'''
Завдання 1
Використовуючи поняття множинного успадкування,
створіть клас «Коло, поміщене в квадрат»
'''
from dataclasses import dataclass
from math import pi


@dataclass
class Square:
    side: int


@dataclass
class Circle:
    def get_circle_square(self, radius):
        return pi * radius ** 2


@dataclass
class CircleInSquare(Square, Circle):
    def get_square_of_circle_in_square(self):
        return self.get_circle_square(self.side / 2)


square_side = 10
circle_in_square = CircleInSquare(square_side)
print(f'Square of circle in square with side={square_side}: {circle_in_square.get_square_of_circle_in_square():.2f}')
