'''
Завдання 2
Створіть клас Passport (паспорт), який міститиме
паспортну інформацію про громадянина заданої країни.
За допомогою механізму успадкування реалізуйте
клас ForeignPassport (закордонний паспорт), похідний
від Passport.
Нагадаємо, що закордонний паспорт містить, крім
паспортних даних, дані про візи і номер закордонного
паспорта.
Кожен із класів має містити необхідні методи.
'''
from dataclasses import dataclass


@dataclass
class NationalPassport:
    _name: str
    _family_name: str
    _address: str
    _passport_number: str

    def get_info(self):
        return f'{self._name} {self._family_name}, {self._address}, {self._passport_number}'


@dataclass
class ForeignPassport(NationalPassport):
    _foreign_passport_number: str
    _visas: list

    def get_info(self):
        return f'National passport: {super().get_info()}\nForeign passport: {self._foreign_passport_number}, visas: {self._visas}\n'

    def add_visa(self, visa_name):
        self._visas.append(visa_name)

    def del_visa(self, visa_name):
        if visa_name in self._visas:
            self._visas.remove(visa_name)
            print(f'Visa "{visa_name}" deleted!')
        else:
            print(f'\nVisa "{visa_name}" not exists!\n')


class Passports(ForeignPassport):
    pass


passports_data = Passports('Tom', 'Jerry', 'Earth','KH0123456', 'HP987456321', ['USA', 'AUSTRALIA'])
print(passports_data.get_info())
passports_data.add_visa('Japan')
passports_data.add_visa('Korea')
print(passports_data.get_info())
passports_data.del_visa('USA')
passports_data.del_visa('USA')
print(passports_data.get_info())



