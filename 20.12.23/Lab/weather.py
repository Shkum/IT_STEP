import json
from threading import Thread
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


# pip install setuptools - если ошибка

class Weather:

    def __init__(self, place='Kyiv'):
        self._place = place
        self._config_dict = get_default_config()
        self._config_dict['language'] = 'ua'
        self._owm = OWM('6447d90ffd2f57c8d4fadf48e2127c01', self._config_dict)
        self._file = 'txt.txt'

    def get_weather(self):
        mgr = self._owm.weather_manager()
        try:
            observation = mgr.weather_at_place(self._place)
            weather = observation.weather
        except:
            return 'Place not exist'
        temp = weather.temperature('celsius')['temp']
        status = weather.detailed_status
        pressure = weather.barometric_pressure()['press']
        rain = weather.rain
        wind = weather.wind()
        res = f'\nWeather in {self._place}:\nTemperature: {temp}\nStatus: {status}\nPressure: {pressure}\nRain: {rain}\nWind: {wind}'
        with open(self._file, 'w', encoding='utf-8') as f:
            f.write(res)
        return res

        # 'barometric_pressure', 'clouds', 'detailed_status', 'dewpoint', 'from_dict',
        # 'from_dict_of_lists', 'heat_index', 'humidex', 'humidity', 'precipitation_probability',
        # 'pressure', 'rain', 'ref_time', 'reference_time', 'snow', 'srise_time', 'sset_time',
        # 'status', 'sunrise_time', 'sunset_time', 'temp', 'temperature', 'to_dict', 'utc_offset',
        # 'uvi', 'visibility', 'visibility_distance', 'weather_code', 'weather_icon_name',

    def set_location(self, new_location):
        self._place = new_location

    def get_location(self):
        return self._place


if __name__ == '__main__':
    weather = Weather()
    weather.set_location('Kyiv')
    t = Thread(target=weather.get_weather)

    t.start()
    t.join()
