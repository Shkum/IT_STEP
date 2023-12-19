'''
Завдання 3
Користувач вводить з клавіатури шлях до існуючої та
до нової директорії. Після чого запускається потік, який має
скопіювати вміст директорії у нове місце. Збережіть структуру
директорії. Виведіть статистику виконаних операцій на екран
'''

from shutil import copytree, rmtree
from threading import Thread
from sys import stdout
from time import sleep
import os

src_dir = os.path.dirname(os.getcwd())
new_dir = os.path.join(os.path.dirname(os.getcwd()), 'new_dir')


# src_dir = input('Enter path to source directory: ')
# new_dir = input('Enter path to new directory: ')

def pauza(count=30):
    for i in range(count):
        stdout.write(f'\r{"~" * (i + 1)}')
        sleep(0.1)


def copy_dir(src_path, new_path):
    if os.path.exists(src_path):
        if os.path.exists(new_path):
            print(f'\nTarget directory already exists.\nRemoving...')
            pauza()
            rmtree(new_path)
        print(f'\n\nCopying directory "{src_path}" to "{new_path}"')
        pauza()
        copytree(src_path, new_path)
        print(f'\n\nCopying of directory "{src_path}" to path "{new_path}" completed')
    else:
        print(f'\nSource directory "{src_path}" not exists.\nExiting...')


t = Thread(target=copy_dir, args=(src_dir, new_dir))

t.start()

t.join()

print('\nDone!')