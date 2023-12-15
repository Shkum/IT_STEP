'''
Завдання 3
До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
використанням json та pickle
'''
import json
import pickle


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.json = 'json.json'
        self.pickle = 'file.pickle'

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

    def save_json(self):
        with open(self.json, 'w') as f:
            json.dump(self.__dict__, f)
            print('\nJSON Data saved')

    def load_json(self):
        with open(self.json) as f:
            res = dict(json.load(f))
            self.numerator, self.denominator, self.json, self.pickle = res.values()
            print('\nJSON Data loaded')

    def save_pickle(self):
        with open(self.pickle, 'wb') as f:
            pickle.dump(self, f)
            print('\nPICKLE Data saved')

    def load_pickle(self):
        with open(self.pickle, 'rb') as f:
            self = pickle.load(f)
            print('\nPICKLE Data loaded\n')


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

fract1.save_json()
fract1.load_json()

fract2.save_pickle()
fract2.load_pickle()

print((fract1 + fract2).short())
