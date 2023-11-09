'''
Завдання 2
Створіть клас для конвертування температури з Цельсія
у Фаренгейт, і навпаки. У класі має знаходитися два статичні
методи: для конвертування з Цельсія у Фаренгейт і для конвертування з
Фаренгейта у Цельсій. Також клас має розрахувати
кількість підрахунків температури та повернути це значення
статичним методом.
'''


class ConverterCtoF:
    counter = 0

    @staticmethod
    def cels_to_farhr(celsius: float):
        ConverterCtoF.counter += 1
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahr_to_celsius(fahrenheit: float):
        ConverterCtoF.counter += 1
        return (fahrenheit - 32) * 5 / 9


print(ConverterCtoF.cels_to_farhr(15), 'F')
print(ConverterCtoF.fahr_to_celsius(59), 'C')
print('Quantity of convertor:', ConverterCtoF.counter)
