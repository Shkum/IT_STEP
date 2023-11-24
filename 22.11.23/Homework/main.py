'''
Завдання 3
Створіть метаклас, який автоматично додає певні
атрибути до всіх класів, що використовують його
'''


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['new_attr'] = 'New attribute'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    attr = 10

    def method(self):
        pass


obj = MyClass()
print(obj.attr)
print(obj.new_attr)
