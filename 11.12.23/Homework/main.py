'''
Завдання 2
Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
даних (використовуючи стиснення та розпакування).
'''

import pickle
import gzip

music_dict = {
    'The Beatles': ['Abbey Road', 'Sgt. Pepper\'s Lonely Hearts Club Band', 'Revolver'],
    'Queen': ['A Night at the Opera', 'The Game', 'News of the World'],
    'Led Zeppelin': ['IV', 'Physical Graffiti', 'Led Zeppelin II'],
    'Pink Floyd': ['The Dark Side of the Moon', 'Wish You Were Here', 'Animals'],
    'The Rolling Stones': ['Exile on Main St.', 'Sticky Fingers', 'Let It Bleed'],
    'U2': ['The Joshua Tree', 'Achtung Baby', 'War'],
    'Radiohead': ['OK Computer', 'Kid A', 'In Rainbows'],
    'Nirvana': ['Nevermind', 'In Utero', 'MTV Unplugged in New York'],
    'The Doors': ['The Doors', 'L.A. Woman', 'Strange Days'],
    'Metallica': ['Master of Puppets', 'Metallica (The Black Album)', 'Ride the Lightning']
}


class Countries:

    def __init__(self):
        self.data = {}
        self.file = 'data.gz'

    def __str__(self):
        return f'{self.data}'

    def add_band(self, band, album):
        self.data[band] = album
        print(f'Band added: "{band}"')

    def del_band(self, band):
        if band in self.data:
            del self.data[band]
            print(f'Band deleted: "{band}"')
        else:
            print(f'Band not found: "{band}"')

    def search_band(self, band):
        if band in self.data:
            print(f'Band "{band}" found with albums "{self.data[band]}"')
        else:
            print(f'Band not found: "{band}"')

    def add_album(self, band, album):
        if band in self.data:
            self.data[band].append(album)
            print(f'Album added: {album}')
        else:
            print(f'Band not found: "{band}"')

    def save_data(self):
        with gzip.open(self.file, 'wb', compresslevel=9) as file:
            file.write(pickle.dumps(self))

    def load_data(self):
        with gzip.open(self.file, 'rb') as file:
            return pickle.loads(file.read())


obj = Countries()
obj.data = music_dict
print('\nCREATE MUSIC DICT\n')
[print(x, y) for x, y in obj.data.items()]
print('\nADD NEW BAND\n')
obj.add_band('Vopli Vidoplyasova', ['Kraina Mriy', "Tantsi", 'Fayno'])
print('\nSHOW DICT WITH NEW BAND\n')
[print(x, y) for x, y in obj.data.items()]
print('\nADD NEW ALBUM\n')
obj.add_album('Vopli Vidoplyasova', 'Abo Abo')
print('\nSHOW DICT WITH NEW ALBUM\n')
[print(x, y) for x, y in obj.data.items()]
print('\nSEARCH BAND\n')
obj.search_band('Nirvana')
print('\nSAVE OBJECT\n')
obj.save_data()
print('\nLOAD SAVED OBJECT TO NEW VARIABLE\n')
obj2 = obj.load_data()
print('\nPRINT NEW OBJECT\n')
print(obj2)
print('\n')
[print(x, y) for x, y in obj.data.items()]
print('\nDELETE BAND\n')
obj2.del_band('Pink Floyd')
print('\nSHOW DICT WITHOUT DELETED BAND\n')
[print(x, y) for x, y in obj2.data.items()]


