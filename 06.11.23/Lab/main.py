'''
Завдання 4
Створіть клас "Комп'ютер", який має зберігати
інформацію про процесор, ОЗУ та відеокарту. Застосуйте
інкапсуляцію для захисту цих даних від змін.
'''
from dataclasses import dataclass


@dataclass
class Computer:
    _cpu: str
    _ram: int
    _video: str

    def __str__(self):
        return f'\nCpu: {self._cpu}\nRAM: {self._ram}\nVideo: {self._video}\n'

    def set_cpu(self, cpu):
        self._cpu = cpu

    def get_cpu(self):
        return self._cpu

    def set_ram(self, ram):
        self._ram = ram

    def get_ram(self):
        return self._ram

    def set_video(self, video):
        self._video = video

    def get_video(self):
        return self._video


pc = Computer('i9 4000', 64, 'Geforce 12GB')
print(pc)
pc.set_cpu('i7 2100')
pc.set_ram(16)
pc.set_video('Geforce 2GB + 2GB')
print(pc)
