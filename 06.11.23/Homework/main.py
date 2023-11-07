'''
Завдання 2
Розробіть систему управління замовленнями таксі.
Кожне замовлення має містити інформацію про
клієнта, адресу, тип автомобіля та вартість. Реалізуйте
методи для додавання нових замовлень, зміни адреси та
типу автомобіля, а також видалення замовлення.
Використайте інкапсуляцію для захисту вартості від
неправильних змін.
'''


class TaxiOrders:
    '''Create and manage taxi`s orders'''


    def __init__(self):
        self.__orders = {}

    def __str__(self):
        return str(self.__orders)

    def add_order(self, client, address, auto_type, price):
        self.__orders[client] = {'address': address, 'auto_type': auto_type, 'price': price}
        print(f'Order "{client}" added successfully')

    def change_address(self, client, new_address):
        if client in self.__orders:
            self.__orders[client]['address'] = new_address
            print(f'Address of "{client}" successfully changed')
        else:
            print(f'Client "{client}" not found')

    def change_auto(self, client, new_auto):
        if client in self.__orders:
            self.__orders[client]['auto'] = new_auto
            print(f'Auto of "{client}" successfully changed')
        else:
            print(f'Client "{client}" not found')

    def del_order(self, client):
        if client in self.__orders:
            del self.__orders[client]
            print(f'Client "{client}" successfully deleted')
        else:
            print(f'Client "{client}" not found')


orders = TaxiOrders()

orders.add_order('Cinderella', 'Fairytale', 'Tykva GTX', 500)
orders.add_order('Pinocchio', 'Fairytale 2', 'Dlinniy nos', 300)
print(orders)
orders.change_address('Cinderella', 'Fairytale 1')
print(orders)
orders.change_auto('Kurochka ryaba', 'lisapet')
orders.change_auto('Pinocchio', 'Moped')
print(orders)
orders.add_order('Kolobok', 'Fairytale 3', 'kolobok', 100)
print(orders)
orders.del_order('kolobok')
orders.del_order('Kolobok')
print(orders)


