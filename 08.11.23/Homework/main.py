'''
Завдання 4
Створіть клас InformationSystem, який має атрибут data
- словник, де ключі - це імена користувачів, а значення -
список їх контактів. Реалізуйте методи класу для додавання
нових користувачів та їх контактів.
'''


class InformationSystem:
    _data = {}

    @classmethod
    def add_user(cls, user):
        if user not in cls._data:
            cls._data[user] = []
            print('User added!')
        else:
            print('User already exists!')

    @classmethod
    def add_user_contacts(cls, user, *args):
        if user in cls._data:
            for contact in args:
                cls._data[user].append(contact)
            print("User contacts added!")
        else:
            print('User not found!')

    @classmethod
    def get_data_info(cls):
        return cls._data


InformationSystem.add_user('ITStep')
print(InformationSystem.get_data_info())
InformationSystem.add_user_contacts('ITStep', '987654321', 'da@da.da', 'net@net.net')
print(InformationSystem.get_data_info())
InformationSystem.add_user('Kraken')
print(InformationSystem.get_data_info())
InformationSystem.add_user_contacts('Kraken', '0123456789', 'das@das.das', 'nets@nets.nets')
print(InformationSystem.get_data_info())


