'''
Завдання 1
Створіть систему управління замовленнями
готелю. Кожне замовлення має містити інформацію
про клієнта, тип кімнати, кількість днів проживання та
вартість. Реалізуйте методи для додавання замовлення,
зміни типу кімнати та кількості днів, а також
видалення замовлення. Використайте інкапсуляцію для
захисту вартості від неправильних змін.
'''


class Booking:
    '''\nClass for creation and managing of order list for booking\n'''

    _client: str
    _room: str
    _period_days: int
    _price_per_day: float

    __orders = {}

    def __str__(self):
        return str(self.__orders)

    def add_order(self, client, room, period, price):
        self.__orders[client] = [room, period, price]

    def change_room(self, client, new_room):
        if client in self.__orders:
            self.__orders[client][0] = new_room
        else:
            print('Client not found!')

    def change_period(self, client, new_period):
        if client in self.__orders:
            self.__orders[client][1] = new_period
        else:
            print('Client not found!')

    def delete_order(self, client):
        if client in self.__orders:
            del self.__orders[client]
        else:
            print('Client not found!')

    def get_total_price(self, client=None):
        if not client:
            res = 0
            for order, (room, period, price) in self.__orders.items():
                res += period * price
            return res
        else:
            if client in self.__orders:
                return self.__orders[client][-2] * self.__orders[client][-1]
            else:
                return 'Client not found!'


order_list = Booking()
print(order_list.__doc__)
order_list.add_order('Tom', '1 room, common', 2, 100)
order_list.add_order('Jerry', '1 room, lux', 3, 300)
print(order_list)
print(f'\nTotal price for all orders: {order_list.get_total_price()}')
print(f'Total price for Tom: {order_list.get_total_price("Tom")}')
print(f'Total price for Jerry: {order_list.get_total_price("Jerry")}')
print(f'Total price for Tor: {order_list.get_total_price("Tor")}')
print('\nAdd Mars to order list...\n')

order_list.add_order('Mars', '1 room, econom', 3, 50)

print(f'Total price for all orders: {order_list.get_total_price()}')
print(order_list)
print('\nDelete Mars from order list...')
order_list.delete_order('Mars')
print(order_list)
