'''
Завдання 2
Для класів із першого завдання перевизначте магічні
методи int (повертає площу) та str (повертає інформацію
про фігуру).
'''

from dataclasses import dataclass


@dataclass
class Figure:
    def square(self):
        pass

    def __int__(self):
        return int(self.square())

    def __str__(self):
        return f'Current figure name is "{self.__class__.__name__}"'


@dataclass
class Rectangle(Figure):
    sideA: float
    sideB: float

    def square(self):
        return self.sideA * self.sideB


@dataclass
class Circle(Figure):
    radius: float

    def square(self):
        pi = __import__('math').pi
        return pi * self.radius ** 2


@dataclass
class RightTriangle(Figure):
    legA: float
    legB: float

    def square(self):
        return (self.legA * self.legB) / 2


@dataclass
class Trapezoid(Figure):
    baseA: float
    baseB: float
    height: float

    def square(self):
        return (self.baseA + self.baseB) * self.height / 2


rectangle = Rectangle(5, 10)
circle = Circle(10)
triangle = RightTriangle(6, 8)
trapezoid = Trapezoid(10, 20, 15)

print(f'Square of rectangle is: {rectangle.square():.2f}')
print(f'Square of circle is: {circle.square():.2f}')
print(f'Square of triangle is: {triangle.square():.2f}')
print(f'Square of trapezoid is: {trapezoid.square():.2f}')
print('$' * 30)
print(rectangle)
print(circle)
print(triangle)
print(trapezoid)
print('$' * 30)
print('Rectangle square:', int(rectangle))
print('Circle square:', int(circle))
print('Right triangle square:', int(triangle))
print('Trapezoid square:', int(trapezoid))


