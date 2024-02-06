import redis
import bcrypt
import json
import datetime


class NotebookApp:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=1):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

    def add_user(self, username, password):
        if self.redis.hexists('users', username):
            print('User already exists')
            return False
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {
            'password_hash': password_hash.decode('utf-8'),
            'full_name': '',
            'friends': [],
            'posts': []
        }
        self.redis.hset('users', username, json.dumps(user_data))
        return True

    def login(self, username, password):
        stored_user_data = self.redis.hget('users', username)
        if stored_user_data:
            user_data = json.loads(stored_user_data)
            stored_password_hash = user_data.get('password_hash')
            if stored_password_hash and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                print(f'Logged in as "{username}"')
                self.current_user = username
                return True
            print("Wrong user name or password")
            return False

    def add_note(self, note_id, note):
        if self.redis.hexists('notes', note_id):
            print('Note already exists')
            return False
        note_data = {
            'note': note,
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.redis.hset('notes', note_id, json.dumps(note_data))
        return True

    def delete_note(self, note_id):
        if self.redis.hexists('notes', note_id):
            self.redis.hdel('notes', note_id)
            print('Note deleted')
        else:
            print('Note not found')

    def edit_note(self, note_id, new_data):
        if not self.redis.hexists('notes', note_id):
            print('Note not found')
            return
        self.redis.hset('notes', note_id, new_data)
        print('Note data updated')

    def view_all_notes(self):
        notes = self.redis.hgetall('notes')
        print(notes)

    def view_allnotes(self):
        notes = self.redis.hgetall('notes')
        print(notes)

    def view_notes_in_time_range(self, time_start, time_end):
        notes = self.redis.hgetall('notes')
        result = []
        for note in notes:
            time = json.loads(notes[note]['time'])
            if time_start < time < time_end:
                result.append(note)
        print(result)

    def view_notes_with_words(self, word_list: list):
        notes = self.redis.hgetall('notes')
        result = []
        for note in notes:
            note_list = json.loads(notes[note])['note'].split()
            if len(set(note_list) & set(word_list)):
                result.append(f'{note}: {notes[note]}')
        print(result)


menu = '''\n    MENU:
1 - Login
2 - Add note
3 - Delete note
4 - Edit note
5 - Review notes
6 - View all notes
7 - View notes in time range
8 - View notes with words
0 - Exit

Enter your choice: '''

note = NotebookApp()

while True:
    choice = input(menu)
    match choice:
        case '1':
            note.login(input('Enter User name: '), input('Enter user password: '))
        case '2':
            note.add_note(input('Enter note id: '), input('Enter note: '))
        case '3':
            note.delete_note(input('Enter note id: '))
        case '4':
            note.edit_note(input('Enter note id: '), input('Enter new data: '))
        case '5':
            note.view_all_notes()
        case '6':
            note.view_allnotes()
        case '7':
            note.view_notes_in_time_range(input('Enter start time: '), input('Enter end time: '))
        case '8':
            note.view_notes_with_words(input('Enter words divided by space: ').split())
        case '0':
            print('Exiting...')
            break
