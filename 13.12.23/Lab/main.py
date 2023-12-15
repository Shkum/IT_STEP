'''
Завдання 2
Реалізація програми для додавання, видалення та
відстеження завдань/заміток. Зберігати ці завдання у
форматі JSON у файлі. Можливість завантаження
раніше збережених завдань для подальшої роботи з
ними
'''
import json
import os


class Notes:

    def __init__(self):
        self._notes = {}
        self._file = 'json.json'
        self.load_notes()
        self._d_key = 0 if not self._notes else int(list(self._notes.keys())[-1])

    def add_note(self, note):
        if  note not in self._notes.values():
            self._notes[str(self._d_key + 1)] = note
            self._d_key += 1
            print('\nNote added')
        else:
            print('\nNote already exists')

    def del_note(self, d_key):
        if d_key in self._notes:
            del self._notes[d_key]
            print('\nNote deleted')
        else:
            print('\nNote not found')

    def load_notes(self):
        if os.path.exists(self._file):
            with open(self._file) as f:
                self._notes = json.loads(f.read())
            print('\nNotes loaded')
        else:
            print('\nNotes not loaded')

    def save_notes(self):
        with open(self._file, 'w') as f:
            f.write(json.dumps(self._notes))
        print("\nNotes saved")

    def edit_note(self, d_key):
        if d_key in self._notes:
            new_note = input('\nEnter new note: ')
            self._notes[str(d_key)] = new_note
            print('\nNote updated')
        else:
            print('\nNote not found')

    def show_all_notes(self):
        for k, v in self._notes.items():
            print(k, v)


note = Notes()

note.add_note('Tili-tili trali-vali')
note.save_notes()
note.add_note('Abra shvabra cadabra')
note.add_note('Sim-silibim')
note.add_note('Ahalay - mahalay')
note.save_notes()
print()
note.show_all_notes()
note.del_note('1')
print()
note.show_all_notes()
note.edit_note('2')
print()
note.show_all_notes()
