'''
Завдання 3
Створіть клас "Електронний Гаманець" додавши
можливість видаляти та додавати гроші, а також перевіряти
баланс.
'''
from dataclasses import dataclass


@dataclass
class ElectronicWallet:
    _name: str
    __balance: float

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_balance(self):
        return self.__balance

    def add_balance(self, amount):
        self.__balance += amount

    def sub_balance(self, amount):
        if self.__balance - amount < 0:
            print(f'Error: balance can not be negative! [{self.__balance - amount}]')
        else:
            self.__balance -= amount

    def __str__(self):
        return f'{self._name}: {self.__balance}'


account = ElectronicWallet('Petro', 100)
print(account)
account.set_balance(150)
print(account.get_balance())
print(account)
account.add_balance(20)
print(account)
account.sub_balance(180)
print(account)
