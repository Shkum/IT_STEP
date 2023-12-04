'''
Завдання 2
Створіть клас черги з пріоритетами для роботи із символьними значеннями.
Ви маєте створити реалізації для операцій над елементами черги:
■ IsEmpty — перевірка, чи черга пуста;
■ IsFull — перевірка черги на заповнення;
■ InsertWithPriority — додати елемент з пріоритетом у чергу;
■ PullHighestPriorityElement — видалення елемента з найвищим пріоритетом із черги;
■ Peek — повернення найбільшого за пріоритетом елемента. Зверніть увагу, що елемент не видаляється з черги;
■ Show — відображення на екрані всіх елементів черги. Показуючи елемент, також необхідно вказати і його пріоритет.
На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.
'''

from collections import deque


class MyCherga:
    def __init__(self, maxlen=None):
        self.__que = deque(maxlen=maxlen)

    def __str__(self):
        res = []
        for q in self.__que:
            res.append(f'({q[0]}, {q[1]})')
        return '->'.join(res)

    def is_empty(self):
        return not len(self.__que)

    def is_full(self):
        return len(self.__que) == self.__que.maxlen

    def enqueue(self, value, priority):
        if len(str(value)) == 1 and len(str(priority)) == 1:
            self.__que.append((str(value), priority))
            self.__que = deque(sorted(self.__que, key=lambda x: x[1]))
        else:
            print('Wrong value or priority')

    def dequeue(self):
        if len(self.__que) > 0:
            return self.__que.popleft()
        else:
            return 'Queue is empty'

    def show(self):
        return self


test = MyCherga(maxlen=5)

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
            val = input('Enter symbol and priority separated by spase to add (ex: a 1): ').split()
            if len(val) == 2:
                test.enqueue(val[0], val[1])
            else:
                print('Wrong data entered')
                continue
        case '4':
            test.dequeue()
        case '5':
            print(test.show())
            continue
        case _:
            print('\nExiting...')
            break
    print(f'\n{test}\n')
