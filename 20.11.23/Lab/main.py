'''
Завдання 2
Створіть дескриптор для атрибуту, що зберігає
розмір файлу. Додайте можливість зберігати розмір
файлу в байтах, але представляти його у зручному для
читання форматі (наприклад, КБ або МБ).
'''

class FileSizeDescriptor:
    size_bytes = 0

    def __get__(self, instance, owner):
        return self.formatted()

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("File size must  be positive")
        self.size_bytes = value

    def formatted(self):
        if self.size_bytes < 1024: return f'{self.size_bytes} b'
        elif self.size_bytes < 1024 ** 2: return f'{self.size_bytes / 1024:.2f} Kb'
        elif self.size_bytes < 1024 ** 3: return f'{self.size_bytes / 1024 ** 2:.2f} Mb'
        else: return f'{self.size_bytes / 1024 ** 3:.2f} Gb'


class File:
    size = FileSizeDescriptor()


file = File()
file.size = 2033000000
print(file.size)
file.size = 20330000
print(file.size)
file.size = 203300
print(file.size)

