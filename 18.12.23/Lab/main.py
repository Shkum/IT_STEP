'''
Завдання 2
Користувач вводить з клавіатури значення у список.
Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку.
Другий потік знаходить середнє арифметичне у списку. Результати обчислень
виведіть на екран.
'''

from random import randint as rnd
from threading import Thread

# s = [int(input('Enter number: ')) for _ in range(10)]

s = [rnd(1, 100) for _ in range(10)]

print('List:', s, '\n')


def find_sum(nums: list):
    print('Sum:', sum(nums))


def find_mean(nums: list):
    print('Mean:', sum(nums) / len(nums))


t1 = Thread(target=find_sum, args=(s,))
t2 = Thread(target=find_mean, args=(s,))

t2.start()
t1.start()

t1.join()
t2.join()
