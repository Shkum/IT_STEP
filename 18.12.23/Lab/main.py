'''Завдання 3
Користувач вводить з клавіатури шлях до файлу, що
містить набір чисел. Після чого запускаються два потоки.
Перший потік створює новий файл, в який запише лише
парні елементи списку. Другий потік створює новий файл,
в який запише лише непарні елементи списку. Кількість
парних і непарних елементів виводиться на екран.'''

from threading import Thread
from random import randint as rnd

# file = input('Enter file name: ')
file = 'nums.txt'


even = []
odd = []

with open(file, 'w') as f:
    for i in range(100):
        print(rnd(10, 100), file=f)


def get_even(file):
    global even
    with open(file) as fr, open('even.txt', 'w') as fw:
        even = [x for x in fr.readlines() if not int(x) & 1]
        for num in even:
            print(num, file=fw, end='')


def get_odd(file):
    global odd
    with open(file) as fr, open('odd.txt', 'w') as fw:
        odd = [x for x in fr.readlines() if int(x) & 1]
        for num in odd:
            print(num, file=fw, end='')


t1 = Thread(target=get_even, args=(file,))
t2 = Thread(target=get_odd, args=(file,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Even:', len(even))
print('Odd:', len(odd))

