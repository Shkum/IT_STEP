'''
Завдання 3
До вже реалізованого класу «Стадіон» додайте можливість
стиснення та розпакування даних з використанням json та
pickle.
'''

import json
import pickle

from dataclasses import dataclass


@dataclass
class Stadium:
    name: str
    open_date: str
    country: str
    city: str
    capacity: int

    def __str__(self):
        return self.name

    def __sub__(self, other):
        return abs(self.capacity - other.capacity)

    def __add__(self, other):
        return abs(self.capacity + other.capacity)

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity


class StadiumWithSave(Stadium):
    def __init__(self, name, open_date, country, city, capacity):
        super().__init__(name, open_date, country, city, capacity)
        self.json = 'file.json'
        self.pickle = 'file.pickle'

    def save_json(self):
        with open(self.json, 'w') as f:
            json.dump(self.__dict__, f)
            print('\nJSON Data saved')

    def load_json(self):
        with open(self.json) as f:
            res = dict(json.load(f))
            print('\nJSON Data loaded\n')
            return res

    def save_pickle(self):
        with open(self.pickle, 'wb') as f:
            pickle.dump(self, f)
            print('\nPICKLE Data saved')

    def load_pickle(self):
        with open(self.pickle, 'rb') as f:
            obj = pickle.load(f)
            print('\nPICKLE Data loaded\n')
            return obj


stadium1 = StadiumWithSave('Wembley', '2007', 'United Kingdom', 'London', 90_000)
stadium2 = StadiumWithSave('Azteka', '1966', 'Mexico', 'Mexico City', 87_523)

print(f'Capacity difference between "{stadium1}" and "{stadium2}" is {stadium1 - stadium2} seats')
print(f'Total capacity for "{stadium1}" and "{stadium2}" is {stadium1 + stadium2} seats')
print(f'Is {stadium1} less then {stadium2}: {stadium1 < stadium2}')
print(f'Is {stadium1} bigger then {stadium2}: {stadium1 > stadium2}')

stadium1.save_pickle()
stadium4 = stadium1.load_pickle()
print('--- > Stadium4:', stadium4)

stadium2.save_json()
dic = stadium2.load_json()
for k, v in dic.items():
    stadium4.__setattr__(k, v)

print('--- > Stadium4:', stadium4)

