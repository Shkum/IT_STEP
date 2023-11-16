'''
Завдання 4
Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця. Для базового класу це може бути рядок із написом
«This is Employer class».
Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
інформації, що відповідає кожному типу службовця.
'''
from dataclasses import dataclass


@dataclass
class Employer:
    def print_info(self):
        print(f'This is "{self.__class__.__name__}" class')


@dataclass
class President(Employer):
    pass


@dataclass
class Manager(Employer):
    pass


@dataclass
class Worker(Employer):
    pass


person2 = President()
person2.print_info()

person3 = Manager()
person3.print_info()

person1 = Worker()
person1.print_info()
