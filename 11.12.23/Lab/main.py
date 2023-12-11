'''
Завдання 1
Користувач заповнює з клавіатури список цілих.
Стисніть отримані дані та збережіть їх у файл. Після цього
завантажте дані з файлу в новий список.
'''

import gzip
import pickle
from random import randint as rnd

# list_of_int = [int(input('Enter number: ')) for _ in range(10)]
list_of_int = [rnd(1, 100) for _ in range(10_000)]

data = pickle.dumps(list_of_int)

with gzip.open('file.gz', 'wb', compresslevel=9) as file:
    file.write(data)

with gzip.open('file.gz', 'rb') as file:
    new_data = file.read()
    new_data = pickle.loads(new_data)

print(new_data[:20])
