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
верхнього лівого кута та розмірами.
■ Circle — коло із заданими координатами центру та радіусом.
■ Ellipse — еліпс із заданими координатами верхнього кута
описаного навколо нього прямокутника зі сторонами,
паралельними осям координат, та розмірами цього прямокутника.
Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
фігуру'''
from dataclasses import dataclass
import turtle


@dataclass
class Shape:
    sideA: int = 0
    sideB: int = 0
    left_upper_corner_pos: list = (0, 0)
    radius: int = 0
    center_pos: list = (0, 0)
    rectangle_around_ellipse: list = (0, 0, 100, 200)

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
            f.writelines(f'{self.sideA}\n'
                         f'{self.sideB}\n'
                         f'{self.left_upper_corner_pos}\n'
                         f'{self.radius}\n'
                         f'{self.center_pos}\n'
                         f'{self.rectangle_around_ellipse}')

    def load(self, file_name):
        with open(file_name, encoding='UTF-8') as f:
            lines = f.readlines()
            self.sideA = int(lines[0])
            self.sideB = int(lines[1])
            self.left_upper_corner_pos = eval(lines[2])
            self.radius = eval(lines[3])
            self.center_pos = eval(lines[4])
            self.rectangle_around_ellipse = eval(lines[4])


@dataclass
class Square(Shape):
    pass


@dataclass
class Rectangle(Shape):
    pass


@dataclass
class Circle(Shape):

    def show(self):
        turtle.circle(self.radius)
        turtle.exitonclick()
        turtle.TurtleScreen._RUNNING = True


@dataclass
class Ellipse(Shape):

    def show(self):
        turtle.seth(-45)
        for i in range(2):
            turtle.circle(self.radius, 90)
            turtle.circle(self.radius // 2, 90)
        turtle.exitonclick()
        turtle.TurtleScreen._RUNNING = True


square = Square(200)
rectangle = Rectangle(150, 300, [300, 300])

square.show()
rectangle.show()

circle = Circle(radius=150)
circle.show()

ellipse = Ellipse(radius=150)
ellipse.show()

square.save('square.txt')
rectangle.save('rectangle.txt')
circle.save('circle.txt')
ellipse.save('ellipse.txt')

square.load('square.txt')
rectangle.load('rectangle.txt')
circle.load('circle.txt')
ellipse.load('ellipse.txt')

square.show()
rectangle.show()
circle.show()
ellipse.show()

