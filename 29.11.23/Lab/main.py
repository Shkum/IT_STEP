'''
Завдання 3
Історія дій: Створіть клас Calculator, який
використовує стек для зберігання операцій та
операндів. Методи класу можуть виконувати операції,
зберігаючи їх у стеці для подальшого відновлення
історії обчислень.
'''
from dataclasses import dataclass



class Calculator:
    _calc_string = ''

    def calculate(self, first_num: int, operation: str, second_num: int):
        self._calc_string = f'{first_num}{operation}{second_num}'
        return eval(self._calc_string)
