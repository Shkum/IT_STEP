'''Завдання 3
Створіть базовий клас Shape для рисування плоских фігур.
Визначте методи:
■ Show() — виведення на екран інформації про фігуру;
■ Save() — збереження фігури у файл;
■ Load() — зчитування фігури з файлу.
Визначте похідні класи:
■ Square — квадрат із заданими з координатами лівого
верхнього кута та довжиною сторони.
■ Rectangle — прямокутник із заданими координатами
верхнього лівого кута та розмірами.'''
from dataclasses import dataclass
import turtle


@dataclass
class Shape:
    sideA: int
    sideB: int = 0
    left_upper_corner_pos: list = (0, 0)

    def show(self):
        cur = turtle.Turtle()
        cur.up()
        cur.goto(self.left_upper_corner_pos[0], self.left_upper_corner_pos[1])
        cur.down()
        self.sideB = self.sideB if self.sideB else self.sideA
        cur.forward(self.sideA)
        cur.right(90)
        cur.forward(self.sideB)
        cur.right(90)
        cur.forward(self.sideA)
        cur.right(90)
        cur.forward(self.sideB)
        turtle.exitonclick()
        turtle.TurtleScreen._RUNNING = True

    def save(self, file_name):
        with open(file_name, 'w', encoding='UTF-8') as f:
            f.writelines(f'{self.sideA}\n{self.sideB}\n{self.left_upper_corner_pos}')

    def load(self, file_name):
        with open(file_name, encoding='UTF-8') as f:
            lines = f.readlines()
            self.sideA = int(lines[0])
            self.sideB = int(lines[1])
            self.left_upper_corner_pos = eval(lines[2])


@dataclass
class Square(Shape):
    pass


@dataclass
class Rectangle(Shape):
    pass


square = Square(200)
rectangle = Rectangle(150, 300, [300, 300])

square.show()
rectangle.show()

square.save('square.txt')
rectangle.save('rectangle.txt')

square.load('square.txt')
rectangle.load('rectangle.txt')

square.show()
rectangle.show()
