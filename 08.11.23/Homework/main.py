'''
Завдання 1
До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
класу «Дріб».
'''


class Fraction:
    count = 0
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def short(self):
        i = 1
        while i <= abs(self.numerator):
            if self.numerator % i == 0 and self.denominator % i == 0 and i != 1:
                self.numerator //= i
                self.denominator //= i
            elif self.numerator % i != 0 or self.denominator % i != 0 or i == 1:
                i += 1
        return self

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)

    def __sub__(self, other):
        num = self.numerator * other.denominator - self.denominator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)

    def __truediv__(self, other):
        return self * Fraction(other.denominator, other.numerator)

    @staticmethod
    def get_fractions_quantity():
        return Fraction.count


fract1 = Fraction(1, 5)
fract2 = Fraction(2, 5)
print(fract1 + fract2)
print((fract1 + fract2).short())
print(fract1 - fract2)
print((fract1 - fract2).short())
print(fract1 * fract2)
print((fract1 * fract2).short())
print(fract1 / fract2)
print((fract1 / fract2).short())
print('Fractions quantity:', Fraction.get_fractions_quantity())
