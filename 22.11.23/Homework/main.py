'''
Завдання 4
Метаклас, що додає перевірку та обробку аргументів
__init__ у всіх класах.
'''


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        def new_init(self, *args, **kwargs):
            self.attr = 1_000_000
            self.new_attr = 2_000_000

        dct['__init__'] = new_init

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):

    def __init__(self, attr):
        self.attr = attr

    def method(self):
        pass


obj = MyClass(50)
print(obj.attr)
print(obj.new_attr)
