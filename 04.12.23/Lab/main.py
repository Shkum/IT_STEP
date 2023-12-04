'''
Завдання 1
Створіть клас черги для роботи із символьними значеннями.
Ви маєте створити реалізації для операцій над елементами:
■ IsEmpty — перевірка, чи черга пуста;
■ IsFull — перевірка черги на заповнення;
■ Enqueue — додати новий елемент до черги;
■ Dequeue — видалення елемента з черги;
■ Show — відображення на екрані всіх елементів черги.
На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.
'''

from collections import deque


class MyCherga:
    def __init__(self, maxlen=None):
        self.__que = deque(maxlen=maxlen)

    def __str__(self):
        return '->'.join(list(self.__que))

    def is_empty(self):
        return not len(self.__que)

    def is_full(self):
        return len(self.__que) == self.__que.maxlen

    def enqueue(self, value):
        if len(str(value)) == 1:
            self.__que.append(str(value))
        else:
            print('Value not a symbol')

    def dequeue(self):
        if len(self.__que) > 0:
            return self.__que.popleft()
        else:
            return 'Queue is empty'

    def show(self):
        return '->'.join(list(self.__que))


test = MyCherga(4)

# print('Is empty:', test.is_empty())
# test.enqueue(1)
# test.enqueue(2)
# test.enqueue(3)
# test.enqueue(4)
# print(test.show())
# print('Is full:', test.is_full())
# print('Is empty:', test.is_empty())
# test.dequeue()
# print(test)

menu = '''
1 - Check if queue is empty
2 - Check if queue if full
3 - Enqueue, add new symbol
4 - Dequeue, delete first symbol
5 - Show content of queue
6 - Exit
----> '''

while True:
    sel = input(menu)
    match sel:
        case '1':
            print('Is empty:', test.is_empty())
        case '2':
            print('Is full:', test.is_full())
        case '3':
            test.enqueue(input('Enter symbol to add: '))
        case '4':
            test.dequeue()
        case '5':
            print(test.show())
            continue
        case _:
            print('\nExiting...')
            break
    print(f'\n{test}\n')
