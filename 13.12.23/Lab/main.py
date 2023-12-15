'''
Завдання 1
Розроблення програми з таймером, що підраховує
час. Використати JSON для збереження стану таймера
(наприклад, поточний час) у файлі. При перезапуску
програми відновити час збереженого стану за
допомогою завантаження даних з JSON-файлу
'''

import json
import time
import os

file = 'json.json'
datas = {}


def save_json(data):
    with open(file, 'w') as f:
        data = json.dumps(data)
        f.write(data)


def load_json():
    global datas
    if os.path.exists(file):
        with open(file, 'r') as f:
            data = f.read()
            if data:
                datas = json.loads(data)
        return datas


def show_all_data(data):
    for k, v in data.items():
        print(k, v)



datas = load_json()

if len(datas) == 0:
    print(len(datas))
    print(datas)
    key = 1
    data = ('Script loaded:', time.ctime())
    save_json({key: data})
else:
    key = int(list(datas.keys())[-1]) + 1
    data = ['Script loaded:', time.ctime()]
    datas[key] = data
    save_json(datas)


time.sleep(2)

key = int(list(datas.keys())[-1]) + 1
data = ['Script closed:', time.ctime()]
datas[key] = data
save_json(datas)


show_all_data(datas)



