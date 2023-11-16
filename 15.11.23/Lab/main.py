'''
Завдання 5
Для класів із попереднього завдання реалізуйте магічний метод str,
а також метод int (який повертає вік службовця).
'''
from dataclasses import dataclass


@dataclass
class Employer:
    age: int = 25

    def print_info(self):
        print(f'This is "{self.__class__.__name__}" class')

    def __int__(self):
        return self.age

    def __str__(self):
        return f'This is class "{self.__class__.__name__}"'


@dataclass
class President(Employer):
    pass
    # def __str__(self):
    #     return f'This is class "{self.__class__.__name__}"'


@dataclass
class Manager(Employer):
    pass
    # def __str__(self):
    #     return f'This is class "{self.__class__.__name__}"'


@dataclass
class Worker(Employer):
    pass
    # def __str__(self):
    #     return f'This is class "{self.__class__.__name__}"'


person1 = President()
person1.print_info()

person2 = Manager()
person2.print_info()

person3 = Worker()
person3.print_info()

print('()' * 15)
print(person1)
print(person2)
print(person3)
print('()' * 15)
print(int(person1))
person2.age = 20
print(int(person2))
person3.age = 30
print(int(person3))
