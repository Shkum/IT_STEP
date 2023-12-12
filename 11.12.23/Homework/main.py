'''
Завдання 1
Маємо певний словник з назвами країн і столиць. Назва
країни використовується як ключ, назва столиці — як значення. Реалізуйте:
додавання, видалення, пошук, редагування,
збереження та завантаження даних (використовуючи стиснення та розпакування).
'''

import gzip
import pickle


class Countries:

    def __init__(self):
        self.data = {}
        self.file = 'data.gz'

    def __str__(self):
        return f'{self.data}'

    def add_country(self, country, capital):
        self.data[country] = capital
        print(f'Country added: "{country}"\n')

    def del_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f'Country deleted: "{country}"\n')
        else:
            print(f'Country not found: "{country}"\n')

    def search_country(self, country):
        if country in self.data:
            print(f'Country "{country}" found with capital "{self.data[country]}"\n')
        else:
            print(f'Country not found: "{country}"')

    def change_country(self, country, old_capital, new_capital):
        if country in self.data:
            if old_capital == self.data[country]:
                self.data[country] = new_capital
                print(f'Capital for "{country}" changed to "{new_capital}"\n')
            else:
                print('Wrong capital\n')
        else:
            print(f'Country not found: "{country}"\n')

    def save_data(self):
        with gzip.open(self.file, 'wb', compresslevel=9) as file:
            file.write(pickle.dumps(self))

    def load_data(self):
        with gzip.open(self.file, 'rb') as file:
            return pickle.loads(file.read())


obj = Countries()

obj.add_country('USA', 'Washington')
obj.add_country('France', 'Paris')
obj.add_country('Germany', 'Berlin')
obj.add_country('China', 'Beijing')
obj.add_country('Japan', 'Tokyo')
obj.add_country('Australia', 'Canberra')
obj.save_data()
print("\nObject 1:")
print(obj)
obj.del_country('France')
print(obj)
obj.search_country('USA')
obj.change_country('Japan', 'Tokyo', 'TOKYO')
print('OBJ1', obj)
obj2 = obj.load_data()
print('\nOBJ2', obj2)

