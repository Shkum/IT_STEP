# Завдання 2
# Реалізуйте клієнт-серверний додаток погоди. Клієнт
# звертається до сервера із зазначенням країни та міста.
# Сервер, отримавши запит, видає погоду на тиждень для
# вказаної місцевості. Використовуйте для реалізації додатку багатопотокові механізми.
# Дані про погоду мають бути наперед визначеними та взяті з файлу

import json
from threading import Thread
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


# pip install setuptools - если ошибка

class Weather:

    def __init__(self, place='Kyiv'):
        self.place = place
        self.config_dict = get_default_config()
        self.config_dict['language'] = 'ua'
        self.owm = OWM('6447d90ffd2f57c8d4fadf48e2127c01', self.config_dict)

    def get_weather(self):
        mgr = self.owm.weather_manager()
        observation = mgr.weather_at_place(self.place)
        weather = observation.weather

        temp = weather.temperature('celsius')['temp']
        status = weather.detailed_status
        pressure = weather.barometric_pressure()['press']
        rain = weather.rain
        wind = weather.wind()
        print(f'\nWeather in {self.place}:\nTemperature: {temp}\nStatus: {status}\nPressure: {pressure}\nRain: {rain}\nWind: {wind}')

        # 'barometric_pressure', 'clouds', 'detailed_status', 'dewpoint', 'from_dict',
        # 'from_dict_of_lists', 'heat_index', 'humidex', 'humidity', 'precipitation_probability',
        # 'pressure', 'rain', 'ref_time', 'reference_time', 'snow', 'srise_time', 'sset_time',
        # 'status', 'sunrise_time', 'sunset_time', 'temp', 'temperature', 'to_dict', 'utc_offset',
        # 'uvi', 'visibility', 'visibility_distance', 'weather_code', 'weather_icon_name',

    def set_location(self, new_location):
        self.place = new_location

    def get_location(self):
        return self.place


weather = Weather()
weather.place = 'Kyiv'
t1 = Thread(weather.get_weather())

weather.place = 'Odessa'
t2 = Thread(weather.get_weather())

t2.start()
t1.start()
t1.join()
t2.join()
