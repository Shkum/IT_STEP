
'''
Завдання 1
До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
створених об’єктів класу «Людина».
'''
from datetime import date

print('Task 1')

class Person:
    """\nCreate and manage personal data\n"""

    count = 0

    def __init__(self, name, family_name, date_of_birthday, phone, place_of_birth, country_of_birth):
        self.name = name
        self.family_name = family_name
        self.date_of_birthday = date_of_birthday
        self.phone = phone
        self.place_of_birth = place_of_birth
        self.country_of_birth = country_of_birth
        Person.count += 1

    def print_info(self):
        print(f'\nPersonal data:\nName: {self.name}\n'
              f'Family name: {self.family_name}\n'
              f'Date of berth: {self.date_of_birthday}\n'
              f'Phone number: {self.phone}\n'
              f'Place of birth: {self.place_of_birth}\n'
              f'Country of birth: {self.country_of_birth}\n')

    def __add__(self, other):
        return f'\nAfter wedding: {other.name} {self.family_name}'

    def __str__(self):
        return f'\nPersonal data:\nName: {self.name}\nFamily name: {self.family_name}\n'

    def __sub__(self, other):
        d1 = date.fromisoformat(self.date_of_birthday)
        d2 = date.fromisoformat(other.date_of_birthday)
        return f'\nAge difference: {abs((d1 - d2).days) // 364} years'

    @classmethod
    def get_count_of_instances(cls):
        return cls.count

person = Person('Saruman', 'Shevchenko', '2000-01-01', '123456789', 'Odessa', 'Ukraine')

person.print_info()
person.name = 'Adun'
person.family_name = 'Toridas!'
person.print_info()
print(person)
print(person.__doc__)
print(person.name, person.family_name)

person1 = Person('Tatiana', 'Klichko', '2003-01-01', '987654321', 'Kyiv', 'Ukraine')

print(person + person1)
print(person - person1)

print('\nInstances created:', Person.get_count_of_instances())
