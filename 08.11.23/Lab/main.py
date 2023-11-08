'''
Завдання 3
Створіть клас для підрахунку максимуму з чотирьох
аргументів, мінімуму з чотирьох аргументів, середнє
арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
методів.
'''

import math


class MathOps:

    @staticmethod
    def get_max(*args):
        return max(args)

    @staticmethod
    def get_min(*args):
        return min(args)

    @staticmethod
    def get_mean(*args):
        return sum(args) / len(args)

    @staticmethod
    def get_factorial(num: int):
        return math.factorial(num)


print(MathOps.get_max(10, 20, 30, 40))
print(MathOps.get_min(10, 20, 30, 40))
print(MathOps.get_mean(10, 20, 30, 40))
print(MathOps.get_factorial(5))
