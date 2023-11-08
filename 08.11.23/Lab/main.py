'''
Завдання 4
Створіть клас FileUtils, який має метод класу
count_lines, який приймає шлях до файлу і повертає
кількість рядків у файлі.
'''

class FileUtils:

    @classmethod
    def count_lines(cls, file):
        with open(file, 'r', encoding="UTF8") as f:
            res = len(f.readlines())
        return res

print(FileUtils.count_lines('main.py'))