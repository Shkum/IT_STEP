'''
Завдання 3
Створіть клас для конвертування з метричної системи в
англійську, та навпаки. Реалізуйте функціональність у вигляді
статичних методів. Обов’язково реалізуйте конвертування
заходів довжини.
'''


class Convertor:
    counter = 0

    @staticmethod
    def inch_to_cm(inches: float):
        Convertor.counter += 1
        return round(inches * 2.54, 2)

    @staticmethod
    def cm_to_inch(cm: float):
        Convertor.counter += 1
        return round(cm / 2.54, 2)

    @staticmethod
    def yard_to_metr(yard: float):
        Convertor.counter += 1
        return round(yard * 0.91, 2)

    @staticmethod
    def metr_to_yard(metr: float):
        Convertor.counter += 1
        return round(metr / 0.91, 2)

    @staticmethod
    def mile_to_km(mile: float):
        Convertor.counter += 1
        return round(mile * 1.609, 2)

    @staticmethod
    def km_to_mile(km: float):
        Convertor.counter += 1
        return round(km / 1.609, 2)

    @staticmethod
    def get_convertors_quantity():
        return round(Convertor.counter, 2)


print('10 inches =', Convertor.inch_to_cm(10), 'cm')
print('10 cm =', Convertor.cm_to_inch(10), 'in')
print('10 yards =', Convertor.yard_to_metr(10), 'm')
print('10 metres =', Convertor.metr_to_yard(10), 'yards')
print('10 miles =', Convertor.mile_to_km(10), 'km')
print('10 km =', Convertor.km_to_mile(10), 'miles')
print('\nConvertor used:', Convertor.counter, 'times')
