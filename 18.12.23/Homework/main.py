'''
Завдання 1
При старті додатку запускаються три потоки. Перший
потік заповнює список випадковими числами. Два інші потоки
очікують на заповнення. Коли перелік заповнений, обидва
потоки запускаються. Перший потік знаходить суму елементів
списку, другий потік знаходить середнє арифметичне значення
у списку. Отриманий список, сума та середнє арифметичне
виводяться на екран
'''

from threading import Thread
from random import randint as rnd
from time import sleep

lst = []


def fill_lst(element_count: int):
    global lst
    sleep(1)
    lst = [rnd(1, 1000) for _ in range(element_count)]


def get_sum(lst: list):
    sleep(1)
    print('Sum:', sum(lst))


def get_mean(lst: list):
    sleep(2)
    print('Mean:', sum(lst) / len(lst))


t1 = Thread(target=fill_lst, args=(20,))


# ТУТ ПОЛУЧИЛСЯ ИНТЕРЕСНЫЙ БАГ, РАССКАЖУ НА КУРСАХ ЕСЛИ НЕ ЗАБУДУ :)


# t2 = Thread(target=get_sum, args=(lst,))
# t3 = Thread(target=get_mean, args=(lst,))


t1.start()
t1.join()

print('List', lst)

t2 = Thread(target=get_sum, args=(lst,))
t3 = Thread(target=get_mean, args=(lst,))

t2.start()
t3.start()

t2.join()
t3.join()

print('Done!')
