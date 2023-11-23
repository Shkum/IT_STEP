'''Завдання 1
Задайте метаклас, що автоматично додає
додатковий функціонал до всіх класів, що його
використовують.'''


class AdditionalFunctionMeta(type):
    def __new__(cls, name, bases, dct):
        dct['additional_function'] = lambda self: print(f"Hello from {self.__class__.__name__}!")
        return super().__new__(cls, name, bases, dct)


class MyClass1(metaclass=AdditionalFunctionMeta):
    pass


class MyClass2(metaclass=AdditionalFunctionMeta):
    pass


obj1 = MyClass1()
obj1.additional_function()

obj2 = MyClass2()
obj2.additional_function()

print()

print(dir(MyClass1))
print(dir(MyClass2))
