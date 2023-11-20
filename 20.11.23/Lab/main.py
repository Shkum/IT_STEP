'''
Завдання 1
Створіть клас Calculator, який може виконувати
операції додавання, віднімання, множення та ділення.
Кожна операція буде реалізована як метод класу.
Об'єкт класу Calculator буде функтором, що може
викликатися для виконання обраної операції.
'''


# class Calculator:
#
#     def divide(self, a, b):
#         if not b:
#             raise ZeroDivisionError('You can`t divide by zero')
#         return a / b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def substract(self, a, b):
#         return a - b
#
#     def add(self, a, b):
#         return a + b
#
#     def __call__(self, *args, **kwargs):
#         match args[1]:
#             case '/':
#                 return self.divide(args[0], args[2])
#             case '+':
#                 return self.add(args[0], args[2])
#             case '-':
#                 return self.substract(args[0], args[2])
#             case '*':
#                 return self.multiply(args[0], args[2])


class Calculator:
    def __call__(self, *args, **kwargs):
        match args[1]:
            case '/': return args[0] / args[2] if args[2] else 'Zero division error'
            case '+': return args[0] + args[2]
            case '-': return args[0] - args[2]
            case '*': return args[0] * args[2]


result = Calculator()
print(result(6, '/', 2))
print(result(6, '/', 0))
print(result(6, '+', 2))
print(result(6, '-', 2))
print(result(6, '*', 2))
