'''
Завдання 1
Реалізуйте клас стека роботи з цілими значеннями
(стек цілих). Стек має бути фіксованого розміру.
Реалізуйте набір операцій для роботи зі стеком
o розміщення цілого значення у стеку;
o виштовхування цілого значення зі стеку;
o підрахунок кількості цілих у стеку;
o перевірку, чи порожній стек;
o перевірку, чи повний стек;
o очищення стеку;
o отримання значення без виштовхування
верхнього цілого в стеку.
На старті додатка відобразіть меню, в якому
користувач може вибрати необхідну операцію.
'''

from collections import deque


class Stack:
    _stack = deque(maxlen=3)

    def __str__(self):
        return f'{' -> '.join(map(str, self._stack))}'

    def add_value(self, value: int):
        self._stack.append(int(value))

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
        return self._stack[-1]


s = Stack()

msg = '''   Make your selection:
1 - Add number to stack
2 - Remove number from stak
3 - Length of stack
4 - Is stack empty
5 - Is stack full
6 - Clear stack
7 - Get last value
8 - Exit
---> 
'''

while True:
    sel = input(msg)
    match sel:
        case '1':
            try:
                num = int(input('Enter number to add: '))
                s.add_value(num)
            except BaseException as er:
                print(er)
        case '2':
            s.pop_value()
            print('Last value removed')
        case '3':
            print('Tack length:', s.length())
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
