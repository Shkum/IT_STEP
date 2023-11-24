'''
Завдання 2
Метаклас, що може змінювати ім'я класу залежно
від певних умов або параметрів.
'''


class RenameClassMeta(type):
    def __new__(cls, name, bases, dct):
        new_class_name = name + "_Modified"
        return super().__new__(cls, new_class_name, bases, dct)


class OriginalClass(metaclass=RenameClassMeta):
    pass


obj = OriginalClass()

print(f"Class name: {obj.__class__.__name__}")
