'''
Завдання 4
Створіть базовий клас Clock, який містить атрибути
години та хвилини. Від цього базового класу
успадковуйте два класи: AnalogClock та DigitalClock.
Клас AnalogClock повинен мати метод display_time,
який виводить поточний час у форматі
"години:хвилини". Клас DigitalClock повинен мати
метод display_time, який виводить поточний час у
цифровому форматі "гг:хх".
Створіть об'єкти кожного класу та виведіть
поточний час за допомогою методу display_time.
'''

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Clock:
    times: str

    def display_time(self, clock_type):
        time_list = list(map(lambda x: x.strip(), self.times.split(',')))
        print(f'{clock_type} time now: {time_list[0]}:{time_list[1]}')


@dataclass
class DigitalClock(Clock):

    def display_time(self, clock_type='Digital'):
        super().display_time(clock_type)


@dataclass
class AnalogClock(Clock):
    def display_time(self, clock_type='Analog'):
        super().display_time(clock_type)


user_time = input('Enter time divided by coma (ex: 12,30): ')
display_analog = AnalogClock(user_time)
display_analog.display_time()
display_digital = DigitalClock(user_time)
display_digital.display_time()
print()
user_time = f'{datetime.now().hour}, {datetime.now().minute}'
display_analog = AnalogClock(user_time)
display_analog.display_time()
display_digital = DigitalClock(user_time)
display_digital.display_time()
