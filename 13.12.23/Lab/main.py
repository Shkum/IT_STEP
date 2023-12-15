'''
Завдання 4
До вже реалізованого класу «Годинник» додайте
мож-ливість стиснення та розпакування даних з
використанням json та pickle.
'''

from dataclasses import dataclass
import json
import pickle


@dataclass
class Watch:
    model: str
    maker: str
    year: int
    price: int
    watch_type: str

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return abs(self.price - other.price)

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __mul__(self, other):
        return self.year > other.year

    def __str__(self):
        return f'{self.maker} - {self.model}'


class WatchWithSave(Watch):
    def __init__(self, model, maker, year, price, watch_type):
        super().__init__(model, maker, year, price, watch_type)
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


watch0 = WatchWithSave('G-Shock', 'Casio', 2010, 200, 'wrist')
watch1 = WatchWithSave('G-Shock', 'Casio', 2011, 200, 'wrist')
watch2 = WatchWithSave('Pro-track', 'Casio', 2012, 300, 'wrist')
watch3 = WatchWithSave('Wrist-watch', 'Casio', 2013, 50, 'wrist')

print(f'Is watch0 = watch1: {watch0 == watch1}')
print(f'Is watch0 = watch2: {watch0 == watch2}')
print(watch0)
print(f'Total price for both watches is {watch1 + watch2}')
print(f'Price difference for both watches is {watch1 - watch2}')
print(f'Is watch "{watch1}" more expensive then "{watch2}": {watch1 > watch2}')
print(f'Is watch "{watch1}" cheaper then "{watch2}": {watch1 < watch2}')
print(f'Is watch "{watch2}" newer then "{watch1}": {watch2 * watch1}')

watch3.save_json()

dic = watch3.load_json()

for k, v in dic.items():
    watch0.__setattr__(k, v)

print(f'Is watch0 = watch3: {watch0 == watch3}')

watch0.save_pickle()
watch1 = watch0.load_pickle()

print(f'Is watch0 = watch1: {watch0 == watch1}')



