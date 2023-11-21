'''
Завдання 2
Створіть клас температурного датчика, де обмежується
температура в межах прийнятних для датчика значень, за
допомогою property()
'''


class TempSensor:
    _temp = 0

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, value):
        if 0 < value < 100:
            self._temp = value
            print(f'New temperature {self._temp} received and installed')
        else:
            print(f'Temperature ({value}) out of allowed range!')


temp = TempSensor()

print('Sensor temperature:', temp.temperature)

temp.temperature = 50

print('Sensor temperature:', temp.temperature)

temp.temperature = 120

print('Sensor temperature:', temp.temperature)
