'''
Завдання 2
Створіть клас Ship, який містить інформацію про кораблі.
За допомогою механізму успадкування реалізуйте клас
Frigate (містить інформацію про фрегат), клас Destroyer (містить
інформацію про есмінця), клас Cruiser (містить інформацію
про крейсер).
Кожен із класів має містити необхідні для роботи методи.
'''
from dataclasses import dataclass


@dataclass
class WarShip:
    _name: str
    _model: str
    _size: int
    _crew: int
    _info: str

    def shoot(self):
        print(f'ATTENTION: {self._name} if shooting! Baang!')

    def set_speed(self, speed):
        print(f'{self._name} has current speed: {speed}')

    def stop(self):
        print(f'{self._name} has stopped!')

    def __str__(self):
        return f'{self._name}: {self._model}, {self._size}, {self._crew}, {self._info}'


class Frigate(WarShip):
    def __init__(self, name, model, size, crew, info, cannons):
        super().__init__(name, model, size, crew, info)
        self._cannons = cannons

    def new_method(self):
        print(f'That`s some own method of {self._name}\n')


@dataclass
class Destroyer(WarShip):
    _torpedos: int

    def new_method(self):
        print(f'That`s some own method of {self._name}\n')


@dataclass
class Cruiser(WarShip):
    _paratroopers: int

    def new_method(self):
        print(f'That`s some own method of {self._name}\n')


warship0 = Frigate('Frigate', 'new model', 600_000, 150, 'mid size Frigate', 150)
print(warship0)
warship0.shoot()
warship0.set_speed(20)
warship0.stop()
warship0.new_method()

warship1 = Destroyer('Destroyer', 'new model', 400_000, 150, 'mid size destroyer', 200)
print(warship1)
warship1.shoot()
warship1.set_speed(40)
warship1.stop()
warship1.new_method()

warship2 = Cruiser('Cruiser', 'new model', 500_000, 200, 'mid size cruiser', 50)
print(warship2)
warship2.shoot()
warship2.set_speed(30)
warship2.stop()
warship2.new_method()
