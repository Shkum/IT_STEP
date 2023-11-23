'''
Завдання 2
Створіть метаклас, що перевіряє наявність певних
атрибутів у всіх класах, які використовують цей
метаклас.
'''


class AttributeCheckMeta(type):
    def __new__(cls, name, bases, dct):
        required_attributes = ['attribute1', 'attribute2', 'attribute3']
        missing_attributes = [attr for attr in required_attributes if attr not in dct]
        if missing_attributes:
            raise AttributeError(f"Missing required attributes: {', '.join(missing_attributes)}")
        return super().__new__(cls, name, bases, dct)


class MyClass1(metaclass=AttributeCheckMeta):
    attribute1 = 1
    attribute2 = 2
    attribute3 = 3


class MyClass2(metaclass=AttributeCheckMeta):
    attribute1 = 'a'


obj1 = MyClass1()

obj2 = MyClass2()
