'''
Завдання 4
Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку.
Після чого запускаються двапотоки. Перший потік має знайти файли з потрібним словом
і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого
потоку і проводить виключення усіх заборонених слів (список цих слів потрібно зчитати з файлу
із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран
'''

from threading import Thread
from sys import stdout
from time import sleep
import os

src_dir = os.getcwd()
word = 'Завдання'
new_file = 'new_file.txt'

restricted = 'restricted.txt'
restricted_words = ['Користувач', 'вводить', 'клавіатури', 'шлях', 'існуючої', 'директорії', 'слово', 'для',
                    'пошуку', 'і', 'файлу', 'потік', 'слів', 'з', 'from', 'import', 'restricted', 'open']
with open(restricted, 'w', encoding='UTF-8') as f:
    [print(x, file=f) for x in restricted_words]

if os.path.exists(new_file):
    os.remove(new_file)

# src_dir = input('Enter path to source directory: ')
# word = input('Enter word to search: ')

files = [f for f in os.listdir(src_dir) if os.path.isfile(f)]


def pauza(count=30):
    for i in range(count):
        stdout.write(f'\r{"~" * (i + 1)}')
        sleep(0.1)


def search_in_files(word):
    print(f'\nSearching word "{word}" in files...')
    pauza()
    result = ''
    for file in files:
        with open(file, encoding='UTF-8') as f:
            res = f.read()
        if word in res:
            print(f'\n\nWord "{word}" found. Adding text to file...')
            pauza(5)
            result += res
    with open(new_file, 'w', encoding='UTF-8') as f:
        f.write(result)


def remove_restricted():
    print('\n\nRemoving restricted words...')
    pauza()
    with open(new_file, encoding='UTF-8') as f1, open(restricted, encoding='UTF-8') as f2:
        res = f1.read()
        restr_words = list(map(lambda x: x.strip(), f2.readlines()))
    for word in restr_words:
        if word in res:
            res = res.replace(word, '___')
    print('\n\nRestricted words removed!\n\nUpdating file content...')
    pauza(8)
    with open(new_file, 'w', encoding='UTF-8') as f:
        f.write(res)


t1 = Thread(target=search_in_files, args=(word,))
t1.start()
t1.join()

t2 = Thread(target=remove_restricted())
t2.start()
t2.join()

print('\n\nDone!')
