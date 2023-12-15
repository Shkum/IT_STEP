'''
Завдання 1
Створіть два окремих "мікросервіси" (дві окремі
програми). Одна програма створює та експортує дані у
форматі JSON, а інша програма завантажує та обробляє ці
дані. Це може бути, наприклад, система, яка створює та
обробляє замовлення.
'''

import json
from dataclasses import dataclass

file = 'file.json'


@dataclass
class MicroService1:
    _file: str

    def save_data(self, data):
        with open(self._file, 'w') as f:
            json.dump(data, f)
        print('\nData saved with microservice - 1')


@dataclass
class MicroService2:
    _file: str
    _data: str = None

    def load_data(self):
        with open(self._file) as f:
            res = json.load(f)
        print('\nData loaded with microservice - 2\n')
        return res


service1 = MicroService1(file)
service2 = MicroService2(file)

data = {'1': 'test', '2': 'test2', '3': 'test data'}

service1.save_data(data)

res = service2.load_data().items()
[print(k, v) for k, v in res]
