'''
Завдання 3
Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ,
пароль — як значення. Реалізуйте: додавання, видалення, пошук,
редагування, збереження та завантаження даних (використовуючи стиснення та розпакування).
'''

import gzip
import pickle


class Users:

    def __init__(self):
        self.data = {}
        self.file = 'data.gz'

    def __str__(self):
        return f'{self.data}'

    def add_user(self, login, password):
        self.data[login] = password
        print(f'User added: "{login}"')

    def del_user(self, login):
        if login in self.data:
            del self.data[login]
            print(f'User deleted: "{login}"')
        else:
            print(f'User not found: "{login}"')

    def search_user(self, login):
        if login in self.data:
            print(f'User "{login}" found with password "{self.data[login]}"')
        else:
            print(f'User not found: "{login}"')

    def change_password(self, login, old_password, new_password):
        if login in self.data:
            if old_password == self.data[login]:
                self.data[login] = new_password
                print(f'Password for "{login}" changed to "{new_password}"')
            else:
                print('Wrong password')
        else:
            print(f'User not found: "{login}"')

    def save_data(self):
        with gzip.open(self.file, 'wb', compresslevel=9) as file:
            file.write(pickle.dumps(self))

    def load_data(self):
        with gzip.open(self.file, 'rb') as file:
            return pickle.loads(file.read())


obj = Users()
obj.add_user('test', 'pass')
obj.add_user('root', 'toor')
obj.add_user('toor', 'root')
obj.add_user('login', 'password')
obj.save_data()
print("\nObject 1:")
print(obj)

print("\nObject 2:")
obj2 = obj.load_data()
print(obj2)
print()

obj.del_user('toor')
obj.del_user('toor')
print(obj)
obj.change_password('test', 'pass', 'super_password')
print(obj)
obj.search_user('root')
obj.save_data()

print('\nObject 3:')
obj3 = obj.load_data()
print(obj3)
print()


