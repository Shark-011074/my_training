# >>>>>> РАБОТА С УРОКОМ
# создание функции
from random import random


def say_hello():
    print("Hello")


say_hello()  # Вызов функции

print()


def say_hello_1(name):  # принимающая функция
    print("Hello", name)


say_hello_1(45)
say_hello_1('Grass')

print()

import random


def lottery():  # Возвращающая функция
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(tickets)
    return win


win = lottery()
print('win - ',win)

print()


def lottery_week(Mon, Tue, Wed, Thu, Fri, Sat, Sun):  # функция и принимает и возвращает
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win_1 = random.choice(tickets)
    tickets.remove(win_1)
    win_2 = random.choice(tickets)
    tickets.remove(win_2)
    win_3 = random.choice(tickets)
    tickets.remove(win_3)
    win_4 = random.choice(tickets)
    tickets.remove(win_4)
    win_5 = random.choice(tickets)
    tickets.remove(win_5)
    win_6 = random.choice(tickets)
    tickets.remove(win_6)
    win_7 = random.choice(tickets)
    tickets.remove(win_7)
    print(Mon, Tue, Wed, Thu, Fri, Sat, Sun)
    return win_1, win_2, win_3, win_4, win_5, win_6, win_7


win_1, win_2, win_3, win_4, win_5, win_6, win_7 = lottery_week('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
print(win_1, win_2, win_3, win_4, win_5, win_6, win_7)

print()
print('когда не знаем сколько параметров')


def lottery_3(*args, **kwargs):  # для обычных и именованных параметров
    tickets = [10, 20, 30, 40, 50, 0, 70, 80, 90, 100]
    win_1 = random.choice(tickets)
    tickets.remove(win_1)
    win_2 = random.choice(tickets)
    tickets.remove(win_2)
    win_3 = random.choice(tickets)
    tickets.remove(win_3)
    win_4 = random.choice(tickets)
    tickets.remove(win_4)
    win_5 = random.choice(tickets)
    tickets.remove(win_5)
    win_6 = random.choice(tickets)
    tickets.remove(win_6)
    win_7 = random.choice(tickets)
    tickets.remove(win_7)
    print(*args)
    return win_1, win_2, win_3, win_4, win_5, win_6, win_7


win_1, win_2, win_3, win_4, win_5, win_6, win_7 = lottery_3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "dsfaf")
print(win_1, win_2, win_3, win_4, win_5, win_6, win_7)
print()


def test(a=2, b=True):  # можно сразу задать параметры
    print(a, b)


test('aaa', False)  # переназначили парамметры

print()


def test(a=2, b=True):  # работа со списком в параметрах
    print(a, b)


test([1, 2])

print()


def test(a=2, b=True):  # работа со списком в параметрах
    print(a, b)


test(*[1, 2])  # * распаковывает
print()
print()
print()
# >>>>>> КОНЕЦ РАБОТЫ С УРОКОМ


# >>>>>> ДОМАШНЯЯ РАБОТА

print('Домашняя работа')


def get_matrix(l, c, val_):
    li_l = []
    for n in range(l):
        li_c = []
        li_l.append(li_c)
        for m in range(c):
            li_c.append(val_)
    return li_l
result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)

def get_matrix1(n, m, value):
    matrix1 = []
    for i in range(n):
        matrix1.append([])
        for j in range(m):
            matrix1[i].append(value)
    return matrix1
result_11 = get_matrix1(2, 2, 10)