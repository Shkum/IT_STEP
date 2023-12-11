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
        self._datas = []
        self.file_name = 'data.gz'

    def __str__(self):
        return f'{self._datas}'

    def load_data(self):
        with gzip.open(self.file_name, 'rb') as file:
            data = pickle.loads(file.read())
            print('Data loaded')
        return data

    def save_data(self):
        with gzip.open(self.file_name, 'wb', compresslevel=9) as file:
            file.write(pickle.dumps(self))
        print('Data saved')

    def add(self, data):
        self._datas.append(str(data))
        print(f'Data added: "{data}"')

    def del_data(self, data):
        if data in self._datas:
            self._datas.remove(data)
            print(f'Data removed: "{data}"')
        else:
            print('Data not found')


obj = DataManage()

obj.add('test')
obj.add('tryam')
obj.add('1')
obj.add('2')
print(obj)
obj.save_data()
obj.del_data('tryam')
print(obj)
obj.add('3')
print(obj)
obj2 = obj.load_data()
print(obj2)

menu = '''
       Menu:
1 - Load data
2 - Save data
3 - Add data
4 - Delete data
5 - Exit
----> '''

sel = input(menu)
while sel:
    match sel:
        case '1':
            obj = obj.load_data()
        case '2':
            obj.save_data()
        case '3':
            obj.add(input('Enter value to add: '))
        case '4':
            obj.del_data(input('Enter value to delete: '))
        case _:
            pass
    print('\n', obj, sep='')
    sel = input(menu)
