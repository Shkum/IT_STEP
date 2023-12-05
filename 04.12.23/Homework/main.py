'''
Завдання 1
Розробіть додаток, що імітує чергу запитів до сервера.
Мають бути клієнти, які надсилають запити на сервер, кожен
з яких має свій пріоритет. Кожен новий клієнт потрапляє у
чергу залежно від свого пріоритету. Зберігайте статистику
запитів (користувач, час) в окремій черзі.
Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
'''

from collections import deque
import time


class Queue:
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
        if len(str(priority)) == 1:
            self.__que.append((str(value), priority))
            self.__que = deque(sorted(self.__que, key=lambda x: x[1]))
        else:
            print('Wrong priority')

    def dequeue(self):
        if len(self.__que) > 0:
            return self.__que.popleft()
        else:
            return 'Queue is empty'

    def show(self):
        return self


request = Queue()
user = Queue()
user_name = 'Ser'

menu = '''
1 - Check if queue is empty
2 - Check if queue if full
3 - Enqueue, add new request
4 - Dequeue, delete first request
5 - Show all requests
6 - Exit
----> '''

while True:
    sel = input(menu)
    match sel:
        case '1':
            print('Is empty:', request.is_empty())
        case '2':
            print('Is full:', request.is_full())
        case '3':
            val = input('Enter value and priority separated by spase to add (ex: test 1): ').split()
            if len(val) == 2:
                request.enqueue(val[0], val[1])
                curr_time = time.strftime("%H:%M:%S", time.localtime())
                user.enqueue((user_name, curr_time), val[1])
            else:
                print('Wrong data entered')
            print(f'\n{request}\n')
            print(f'{user}\n')
        case '4':
            request.dequeue()
            user.dequeue()
            print(f'\n{request}\n')
            print(f'\n{user}\n')
        case '5':
            print(request.show())
            print(user.show())
        case _:
            print('\nExiting...')
            break
