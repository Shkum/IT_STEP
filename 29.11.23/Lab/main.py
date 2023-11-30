'''
Завдання 3
Історія дій: Створіть клас Calculator, який
використовує стек для зберігання операцій та
операндів. Методи класу можуть виконувати операції,
зберігаючи їх у стеці для подальшого відновлення
історії обчислень.
'''

from collections import deque


class Stack:
    _stack = deque()

    def __str__(self):
        return f'{list(map(str, self._stack))}'

    def add_value(self, value):
        self._stack.append(value)

    def pop_value(self):
        return self._stack.pop()

    def length(self):
        return len(self._stack)

    def is_empty(self):
        return not bool(self.length())

    def is_full(self):
        return len(self._stack) == self._stack.maxlen

    def clear_stack(self):
        self._stack.clear()

    def get_last_value(self):
        return self._stack[-1] if len(self._stack) else None

    def __iter__(self):
        return iter(self._stack)


class Calculator:
    _calc_string = ''
    _stack = Stack()

    def calculate(self, first_num: int, operation: str, second_num: int):
        self._calc_string = f'{first_num}{operation}{second_num}'
        self._stack.add_value(self._calc_string)
        return eval(self._calc_string)

    def get_last_operation(self):
        return f'{self._stack.get_last_value()}'

    def undo(self):
        self._stack.pop_value()
        self._calc_string = self._stack.get_last_value()
        print("last operation canceled")

    def history(self):
        return self._stack

    def result(self):
        return eval(self._calc_string)


s = Calculator()
s.calculate(5, '*', 25)
print(s.get_last_operation(), s.result(), sep=' = ')
s.calculate(2, '+', 4)
print(s.get_last_operation(), s.result(), sep=' = ')
s.calculate(99, '-', 11)
print(s.get_last_operation(), s.result(), sep=' = ')
print('---> History:', s.history())
print('---> Last expression:', s.get_last_operation())
s.undo()
print('---> History:', s.history())
print('---> Last expression:', s.get_last_operation(), '=', s.result())
