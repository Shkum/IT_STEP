'''
Завдання 1
Користувач вводить з клавіатури значення у список.
Після чого запускаються два потоки. Перший потік знаходить максимум у списку.
Другий потік знаходить мінімум у списку. Результати обчислень виведіть на екран
'''

from random import randint as rnd
from threading import Thread

# s = [int(input('Enter number: ')) for _ in range(10)]

s = [rnd(1, 100) for _ in range(10)]

print('List:', s, '\n')


def find_min(nums: list):
    print('Min:', min(nums))


def find_max(nums: list):
    print('Max:', max(nums))


t1 = Thread(target=find_min, args=(s,))
t2 = Thread(target=find_max, args=(s,))

t2.start()
t1.start()

t1.join()
t2.join()
