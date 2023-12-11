'''
Завдання 2
При старті програми з’являється меню з наступними
пунктами:
1. Завантаження даних;
2. Збереження даних;
3. Додавання даних;
4. Видалення даних.
Використайте список цілих як сховища даних. Також
застосуйте стиснення/розпакування даних
'''

import gzip
import pickle


class DataManage:
    def __init__(self):
        self._data = []
        self.file_name = 'data.gz'

    def __str__(self):
        return f'{self._data}'

    def load_data(self):
        with gzip.open(self.file_name, 'rb') as file:
            self._data = pickle.loads(file.read())
        return self._data

    def save_data(self):
        with gzip.open(self.file_name, 'wb', compresslevel=9) as file:
            file.write(pickle.dumps(self))
        print('Data saved')

    def add(self, data):
        self._data.append(data)
        print(f'Data added: "{data}"')

    def del_data(self, data):
        if data in self._data:
            self._data.remove(data)
            print(f'Data removed: "{data}"')
        else:
            print('Data not found')


obj = DataManage()

obj.add('test')
obj.add('tryam')
obj.add('1')
obj.add(2)
print(obj)
obj.save_data()
obj.del_data('tryam')
print(obj)

obj2 = obj.load_data()
print(obj2)
obj2.del_data('tryam')
print(obj2)
