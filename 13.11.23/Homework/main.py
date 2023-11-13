'''
Завдання 1
Створіть клас Device, який містить інформацію про пристрій.
За допомогою механізму успадкування реалізуйте клас
Coffee Machine (містить інформацію про кавомашину), клас
Blender (містить інформацію про блендер), клас MeatGrinder
(містить інформацію про м’ясорубку).
Кожен із класів має містити необхідні для роботи методи.
'''
from dataclasses import dataclass


@dataclass
class Device:
    _name: str
    _type: str
    _brand: str
    _model: str
    _power: str

    def print_info(self):
        print(f'{self._name}: {self._type}, {self._brand}, {self._model}, {self._power} V.')

    def activate(self, device_name, product):
        print(f'ACTION: {device_name} is ON and preparing {product}')

    def device_OFF(self):
        print(f'{self._name} if OFF\n')


@dataclass
class Coffee(Device):
    def activate(self, device_name='Coffee machine', product='Coffee'):
        super().activate(device_name, product)


@dataclass
class Blender(Device):
    def activate(self, device_name='Blender', product='mix'):
        super().activate(device_name, product)


@dataclass
class MeatGrinder(Device):
    def activate(self, device_name='Meat Grinder', product='ground meat'):
        super().activate(device_name, product)


coffee = Coffee('Coffee maker', 'Automatic coffee machine', 'Bosch', 'Super coffee maker 2023', '220')
coffee.print_info()
coffee.activate()
coffee.device_OFF()
blender = Blender('Blender', 'Automatic blender', 'Kenwood', 'Super blender 2023', '220/110')
blender.print_info()
blender.activate()
blender.device_OFF()
grinder = Blender('Meat Grinder', 'Automatic meat grinder', 'Whirlpool', 'Super meat grinder 2023', '220/110 AC/DC')
grinder.print_info()
grinder.activate()
grinder.device_OFF()

