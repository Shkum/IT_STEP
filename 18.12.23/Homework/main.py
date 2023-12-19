'''
Завдання 2
Користувач вводить з клавіатури шлях до файлу. Після
чого запускаються три потоки. Перший потік заповнює файл
випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений,
обидва потоки стартують. Перший потік знаходить усі прості числа, другий потік
знаходить факторіал кожного числа у файлі. Результати пошуку
кожен потік має записати у новий файл. Виведіть на екран
статистику виконаних операцій.
'''

from threading import Thread
from random import randint as rnd
from time import sleep
from sys import stdout
from math import factorial as fct

file = 'nums.txt'


# file = input('Enter file name: ')

def pauza(count=30):
    for i in range(count):
        stdout.write(f'\r{"~" * (i + 1)}')
        sleep(0.1)


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def fill_file(element_count: int):
    print('Fill up file...')
    pauza()
    with open(file, 'w') as f:
        [print(rnd(1, 35), file=f) for _ in range(element_count)]
    print('\nFilling of file completed!\n')


def get_prime_num():
    print('Getting prime numbers...')
    pauza()
    with open(file) as f:
        res = f.readlines()
    res = [x for x in res if is_prime(int(x))]
    with open('prime_num.txt', 'w') as f:
        [print(i, file=f, end='') for i in res]
    print('\nPrime numbers saved!')


def get_factorial_nums():
    print('\nGetting factorial of numbers...')
    pauza()
    with open(file) as f:
        res = f.readlines()
    res = [fct(int(x)) for x in res]
    with open('factorial_num.txt', 'w') as f:
        [print(i, file=f) for i in res]
    print('\nFactorial numbers saved!')


t1 = Thread(target=fill_file, args=(50,))

t1.start()
t1.join()

t2 = Thread(target=get_prime_num())
t3 = Thread(target=get_factorial_nums())

t2.start()
t3.start()

t2.join()
t3.join()

print('\nDone!')
