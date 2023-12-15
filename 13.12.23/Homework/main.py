'''
Завдання 2
Створіть програму для проведення опитування або
анкетування. Зберігайте відповіді користувачів у форматі
JSON файлу. Кожне опитування може бути окремим
об'єктом у файлі JSON, а відповіді кожного користувача -
списком значень
'''

import json
import os


class Survey:

    def __init__(self):
        self._questions = ['What is your name?: ',
                           'What is your family name?: ',
                           'What is your age?: ',
                           'What is your education?: ']
        self._answers = {}
        self._file = 'file.json'

    def do_survey(self):
        answer = {}
        for question in self._questions:
            resp = input(question)
            if resp:
                answer[question] = resp
            else:
                return
        self._answers[answer['What is your name?: ']] = answer

    def save_data(self):
        with open(self._file, 'w') as f:
            json.dump(self._answers, f)
        print('\nData saved\n')

    def load_data(self):
        if os.path.exists(self._file):
            with open(self._file) as f:
                self._answers = json.load(f)
                print('\nData loaded\n')
        else:
            print('\nFile not found')

    def show_data(self):
        if self._answers:
            for person in self._answers:
                print(person)
                for k, v in self._answers[person].items():
                    print(k, v)
                print()
        else:
            print('\nNo data. File is empty.\n')


survey = Survey()
survey.load_data()
survey.show_data()
survey.do_survey()
print()
survey.do_survey()
print()
survey.do_survey()
print()
survey.do_survey()
survey.save_data()
survey.show_data()


