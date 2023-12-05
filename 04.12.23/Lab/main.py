'''Завдання 3
Розробіть додаток, який дозволяє зберігати інформацію
про логіни і паролі користувачів. Кожному користувачеві
відповідає пара «логін — пароль». При старті додатку
відображається меню:
■ Додати нового користувача;
■ Видалити існуючого користувача;
■ Перевірити, чи існує такий користувач;
■ Змінити логін існуючого користувача;
■ Змінити пароль існуючого користувача.
Для реалізації завдання обов’язково застосуйте одну
із структур даних. При виборі структури керуйтеся постановкою завдання.'''


class User:
    def __init__(self):
        self._lst = {}

    def __str__(self):
        return f'{list(self._lst.items())}'

    def add_new_user(self, login, pas):
        if login and pas:
            self._lst[login] = pas
        else:
            print('Login and password cannot be empty')

    def delete_user(self, login):
        if login in self._lst:
            del self._lst[login]
            print('User deleted')
        else:
            print('User not found')

    def if_exists(self, login):
        if login in self._lst:
            return True
        else:
            return False

    def rename_login(self, old_login, new_login):
        if old_login in self._lst:
            self._lst[new_login] = self._lst[old_login]
            del self._lst[old_login]
            print('Login renamed')
        else:
            print('User not found')

    def change_pas(self, login, old_pass, new_pass):
        if login and old_pass and new_pass:
            if self._lst[login] == old_pass:
                self._lst[login] = new_pass
                print('Password changed')
            else:
                print('Wrong old password')
        else:
            print('Login, old password and new password can not be empty')


menu = '''
1 - Add new user
2 - Delete user
3 - Check if user exists
4 - Change user`s login
5 - Change user`s password
6 - Exit
----> '''

user = User()

while True:
    sel = input(menu)
    match sel:
        case '1':
            user.add_new_user(input('Enter login: '), input('Enter password: '))
        case '2':
            user.delete_user(input('Enter user`s login: '))
        case '3':
            print('User existing:', user.if_exists(input('Enter user`s login: ')))
        case '4':
            user.rename_login(input('Enter old user`s login:'), input('Enter new user`s login:'))
        case '5':
            user.change_pas(input('Enter user`s login:'),
                            input('Enter old user`s password:'),
                            input('Enter new user`s password:'))
        case _:
            print(f'\nExiting...\n')
            break
    print(f'\n{user}\n')
