'''
Завдання 3
Дано три вежі та n дисків різного розміру, відсортованих
за зростанням, розміщених на першій вежі у вигляді піраміди.
Потрібно перемістити всі диски на третю вежу,
використовуючи проміжну вежу, за умови, що можна
переміщати тільки один диск за раз та диск завжди можна
покласти лише на диск більшого розміру або на порожню
вежу.
Ця задача може бути вирішена за допомогою
рекурсивного алгоритму, використовуючи стек для
зберігання проміжних ходів при переміщенні дисків між
вежами
'''

from collections import deque


# Напомните :) показать интересную фишку показывающую разницу между
# статическим и динамическим объявлением атрибута класса :)
class Stack:
    # _stack = deque()
    counter = 0

    def __init__(self):
        self._stack = deque()

    def __str__(self):
        return f'{' -> '.join(map(str, self._stack))}'

    def add_value(self, value):
        self._stack.append(value)

    def pop_value(self):
        Stack.counter += 1
        return self._stack.pop()


def rebuild_towers(n: int, a: Stack, b: Stack, c: Stack):
    if n > 0:
        rebuild_towers(n - 1, a, c, b)
        if a:
            c.add_value(a.pop_value())
        rebuild_towers(n - 1, b, a, c)


n = 15
a = Stack()
for i in range(n):
    a.add_value(n - i)
b = Stack()
c = Stack()
print('Stack a:', a)
print('Stack b:', b)
print('Stack c:', c)

rebuild_towers(n, a, b, c)

print('\nRebuilding of towers ...')
print('\nRebuilding of towers completed\n')
print(f'It takes {Stack.counter} operations\n')

print('Stack a:', a)
print('Stack b:', b)
print('Stack c:', c)


# print(f"\n{'?' * 100}\n")
#
#
# def test_func(x, y, z):
#     print('Stack x:', x)
#     print('Stack y:', y)
#     print('Stack z:', z)
#     x.pop_value()
#     print('Stack x:', x)
#     print('Stack y:', y)
#     print('Stack z:', z)
#     x.pop_value()
#     print('Stack x:', x)
#     print('Stack y:', y)
#     print('Stack z:', z)
#
#
# n = 10
# Stack._stack.clear()
# x = Stack()
# for i in range(n):
#     x.add_value(n - i)
# y = Stack()
# z = Stack()
#
# test_func(x, y, z)
