'''
Завдання 1
Іноді ви можете використати property() для створення
доступу до атрибутів через геттери та сеттери для
забезпечення певних перевірок або операцій перед
отриманням або зміною атрибутів. Створіть клас для
роботи з банківським рахунком, щоб гроші знялися або
зарахувалися тільки при виконанні певних умов
(наприклад, якщо гроші на рахунку є)
'''
from dataclasses import dataclass


@dataclass
class BankAccount:
    _amount: int

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        print('Direct changing of amount is not allowed')

    @property
    def update_amount(self):
        return 'Operation not allowed. Use method "amount" instead.'

    @update_amount.setter
    def update_amount(self, value):
        tmp = self._amount + value
        if tmp < 0:
            print(f'Negative balance ({tmp}) is not allowed')
        elif tmp > 100:
            print('Operation not allowed!')
            print('Update your account for operation with more then 100 currency')
        else:
            self._amount = tmp
            print(f'Account updated! New amount is {self._amount}')


acount = BankAccount(50)
print('On bank account is:', acount.amount)
acount.update_amount = -70
print('On bank account is:', acount.amount)
acount.update_amount = 60
print('On bank account is:', acount.amount)
acount.update_amount = -20
print('On bank account is:', acount.amount)
acount.update_amount = -40
print('On bank account is:', acount.amount)
acount.amount = 20
print('On bank account is:', acount.amount)