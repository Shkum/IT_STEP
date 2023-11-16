'''
Завдання 2
Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
«Колеса», «Двигун», «Двері» та ін
'''
from dataclasses import dataclass


@dataclass
class Wheels:
    wheels_quantity: int
    is_wheels_stopped: bool

    def wheels_turning(self, flag=False):
        self.is_wheels_stopped = flag
        print(f'All {self.wheels_quantity} wheels are', 'stopped' if flag else 'not stopped')


@dataclass
class Engine:
    power: int
    is_engine_stated: bool

    def engine_start(self, flag=False):
        print(f'Engine with power {self.power}HP is {"started" if flag else "not started"}')
        self.is_engine_stated = flag
        return flag


@dataclass
class Doors:
    doors_quantity: int
    is_doors_closed: bool

    def close_doors(self, quant=0, flag=False):
        flag = False if quant else True
        msg = f'{quant} doors of {self.doors_quantity} are opened'
        print(f'All {self.doors_quantity} doors are closed' if flag else msg)
        self.is_doors_closed = flag
        return flag


@dataclass
class Car(Wheels, Engine, Doors):
    def is_car_ready(self):
        if all([self.is_wheels_stopped, self.is_engine_stated, self.is_doors_closed]):
            print(' --> Car is ready')
        else:
            print(' --> Car not ready! check your if wheels are not turning, engine is started and all doors are closed')


car = Car(wheels_quantity=4, is_wheels_stopped=False, power=220, is_engine_stated=False, doors_quantity=5,
          is_doors_closed=False)
# car = Car(4, False, 220, False, 5, False)

car.close_doors(2, False)

car.is_car_ready()
car.close_doors()
car.is_car_ready()

car.wheels_turning()
car.wheels_turning(True)
car.is_car_ready()

car.engine_start(True)

car.is_car_ready()
print()
