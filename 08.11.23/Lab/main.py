'''
Завдання 2
Створіть клас для підрахунку площі геометричних
фігур. Клас має надавати функціональність підрахунку
площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
підрахунку площі реалізуйте за допомогою статичних
методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом.
'''
import math


class Square:

    @staticmethod
    def get_triangle_square_1(a, h):  #
        return 0.5 * a * h

    @staticmethod
    def get_triangle_square_2(a, b, alfa):
        return 0.5 * a * b * math.sin(alfa)

    @staticmethod
    def get_triangle_square_3(a, b, c, r):
        return a * b * c / (4 * r)

    @staticmethod
    def get_rectangle_square(a, b):
        return a * b

    @staticmethod
    def get_square_square(a, b):
        return a * b

    @staticmethod
    def get_rhombus_square(d1, d2):
        return 0.5 * d1 * d2


print('Triangle square:', Square.get_triangle_square_1(5, 6))
print('Triangle square:', Square.get_triangle_square_2(5, 6, 30 / 57.3))
print('Triangle square:', Square.get_triangle_square_3(5, 6, 4, 7))
print('Rectangle square:', Square.get_rectangle_square(5, 6))
print('Square square:', Square.get_square_square(5, 6))
print('Rhombus square:', Square.get_rhombus_square(5, 6))
