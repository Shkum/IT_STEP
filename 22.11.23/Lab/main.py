'''
Завдання 4
Створіть метаклас, який автоматично реєструє всі
нові класи у певному реєстрі для подальшого
використання.
'''


class ClassRegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class


class MyClass1(metaclass=ClassRegistryMeta):
    pass


class MyClass2(metaclass=ClassRegistryMeta):
    pass


print(ClassRegistryMeta.registry)
