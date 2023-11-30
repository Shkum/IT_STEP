'''
Завдання 1
Реалізуйте клас стеку для роботи з рядками (стек рядків).
Стек має бути фіксованого розміру. Реалізуйте набір операцій
для роботи зі стеком:
o розміщення рядка у стек;
o виштовхування рядка зі стеку;
o підрахунок кількості рядків у стеку;
o перевірку, чи порожній стек;
o перевірку, чи повний стек;
o очищення стеку;
o отримання значення без виштовхування
верхнього рядка зі стеку.
На старті додатка відобразіть меню, в якому користувач
може вибрати необхідну операцію.
'''


from collections import deque


class Stack:
    _stack = deque(maxlen=3)

    def __str__(self):
        return f'{' -> '.join(map(str, self._stack))}'

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
        return self._stack[-1] if self.length() else None


s = Stack()

msg = '''   Make your selection:
1 - Add value to stack
2 - Remove value from stak
3 - Get length of stack
4 - Is stack empty
5 - Is stack full
6 - Clear stack
7 - Get last value in stack
8 - Exit
---> 
'''

while True:
    sel = input(msg)
    match sel:
        case '1':
            try:
                num = input('Enter number to add: ')
                s.add_value(num)
            except BaseException as er:
                print(er)
        case '2':
            s.pop_value()
            print('Last value removed')
        case '3':
            print('Stack length:', s.length())
        case '4':
            print('Is stack empty?:', s.is_empty())
        case '5':
            print('Is stack full?:', s.is_full())
        case '6':
            s.clear_stack()
            print('Stack cleared successfully!')
        case '7':
            print('Last value:', s.get_last_value())
        case _:
            print('Exiting...')
            break
    print(f'\n{s}\n')
