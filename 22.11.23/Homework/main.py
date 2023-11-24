'''
Завдання 1
Метаклас, який вносить додаткові перевірки/логіку
до певних методів у всіх класах
'''


class AdditionalLogicMeta(type):
    def __new__(cls, name, bases, dct):
        target_methods = ['method1', 'method3']
        for key, value in dct.items():
            if callable(value) and key in target_methods:
                def wrapper(*args, **kwargs):
                    print(f"Additional logic for {key} is in progress...")
                    result = value(*args, **kwargs)
                    print(f"Additional logic for {key} is complete.")
                    return result

                dct[key] = wrapper
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AdditionalLogicMeta):
    def method1(self):
        print("Executing method1...")

    def method2(self):
        print("Executing method2...")

    def method3(self):
        print("Executing method3...")


my_instance = MyClass()
print(1)
my_instance.method1()
print(2)
my_instance.method2()
print(3)
my_instance.method3()
