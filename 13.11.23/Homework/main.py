'''
Завдання 3
Запрограмуйте клас Money (об’єкт класу оперує однією
валютою) для роботи з грошима.
У класі мають бути передбачені: поле для зберігання цілої
частини грошей (долари, євро, гривні тощо) і поле для
зберігання копійок (центи, євроценти, копійки тощо).
Реалізуйте методи виведення суми на екран, задання
значень частин.
Створіть клас Product для роботи з продуктом або товаром
беручи за основу клас Money. Реалізуйте метод для
зменшення ціни на задане число.
Для кожного з класів реалізуйте необхідні методи та поля.
'''
from dataclasses import dataclass


@dataclass
class Money:
    _bills: int
    _coins: int

    def reduce_amount(self, bills=0, coins=0):
        if self._bills - bills + (self._coins - coins) / 100 >= 0:
            self._bills -= bills
            self._coins -= coins
            self.check_amounts()
        else:
            print('Insufficient funds')

    def add_amount(self, bills=0, coins=0):
        self._bills += bills
        self._coins += coins
        self.check_amounts()

    def check_amounts(self):
        if self._coins > 99:
            self._bills += self._coins // 100
            self._coins %= 100
        elif self._coins < 0:
            self._bills -= 1
            self._coins += 100

    def __str__(self):
        return f'{self._bills}, {self._coins}'


@dataclass
class Euro(Money):
    _currency: str = 'euro'

    def __str__(self):
        return f'{super().__str__()} {self._currency}'


@dataclass
class UAH(Money):
    _currency: str = 'uah'

    def __str__(self):
        return f'{super().__str__()} {self._currency}'


@dataclass
class USD(Money):
    _currency: str = 'usd'

    def __str__(self):
        return f'{super().__str__()} {self._currency}'


@dataclass
class Product:
    item: str
    price: USD

    def __str__(self):
        return f'{self.item}, price: {self.price}'


item = Product('Pineapple', USD(2, 50))
print(item)
item.price.add_amount(1, 30)
print(item)

print()

euro = Euro(2, 150, 'euro')
euro.check_amounts()
print(euro)
euro.add_amount(0, 80)
print(euro)
euro.reduce_amount(4, 0)
print(euro)
euro.reduce_amount(0, 30)
print(euro)
euro.reduce_amount(0, 30)
print(euro)

print()

usd = USD(2, 110, 'usd')
usd.check_amounts()
print(usd)
usd.add_amount(0, 80)
print(usd)
usd.reduce_amount(4, 0)
print(usd)
usd.reduce_amount(0, 30)
print(usd)
usd.reduce_amount(0, 30)
print(usd)

print()

uah = UAH(2, -60, 'uah')
uah.check_amounts()
print(uah)
uah.add_amount(0, 80)
print(uah)
uah.reduce_amount(4, 0)
print(uah)
uah.reduce_amount(0, 30)
print(uah)
uah.reduce_amount(0, 30)
print(uah)