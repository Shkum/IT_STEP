'''
Завдання 2
Реалізуйте клас "Кошик для покупок" з можливістю
додавання товарів та підрахунку загальної вартості.
Застосуйте інкапсуляцію для забезпечення правильності
обробки даних.
'''
from dataclasses import dataclass


@dataclass
class Basket:
    '''Create and manage basket'''

    def __init__(self):
        self._res = {}

    def get_items(self) -> dict:
        return self._res

    def add_item(self, item, price, quantity):
        self._res[item] = price, quantity

    def get_total_price(self):
        res = 0
        for price, quantity in self._res.values():
            res += price * quantity
        return res

    def __str__(self):
        return str(self._res)


basket = Basket()
basket.add_item('orange', 15, 3)
basket.add_item('apple', 20, 2)
basket.add_item('grape', 25, 2)
basket.add_item('mandarin', 30, 5)
print(basket)
print(basket.get_items())
print(f'Total price: {basket.get_total_price()}')
