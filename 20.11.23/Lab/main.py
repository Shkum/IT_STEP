'''
Завдання 3
Створіть клас для представлення відомостей про
замовлення. Забезпечте, щоб номер замовлення був
тільки для читання за допомогою керованих атрибутів,
але його можна було переглядати.
'''
from dataclasses import dataclass


# from dataclasses import dataclass
#
#
# @dataclass
# class OrderReport:
#     _order_number: int
#
#     @property
#     def order_number(self):
#         return self._order_number
#
#     @order_number.setter
#     def order_number(self, new_value):
#         print(f'Order`s number not allowed to be changed to {new_value}')
#
#
# order = OrderReport(150)
# print('Order number is:', order.order_number)
# order.order_number = 100
# print('Order number is:', order.order_number)


class MyDescriptor:
    order_number = 0
    counter = 0

    def __get__(self, instance, owner):
        return self.order_number

    def __set__(self, instance, value):
        if self.counter:
            print('\nValue of order number can not be changed more then 1 time!')
            print(f'Changing order number to {value} is not allowed')
            print('Tries to change order number:', self.counter)
            self.counter += 1
        else:
            self.order_number = value
            print('\nOrder number changed to:', self.order_number)
            self.counter += 1


class MyOrder:
    order_number = MyDescriptor()


order = MyOrder()
print('Order number:', order.order_number)
order.order_number = 500
print('Order number:', order.order_number)
order.order_number = 150
print('Order number:', order.order_number)
order.order_number = 160
print('\nOrder number:', order.order_number)
order.order_number = 170
print('\nOrder number:', order.order_number)
order.order_number = 180
print('\nOrder number:', order.order_number)
order.order_number = 190
print('\nOrder number:', order.order_number)