import random


def key():
    password = ''
    ar1 = random.randint(3, 20)  # создаем случайное число
    print(ar1)
    for num_1 in range(1, ar1):  # перебираем первое число пары
        for num_2 in range(1, ar1):  # перебираем второе число пары
            if num_2 > num_1:  # при итерации второе число пары всегда БОЛЬШЕ первого
                if ar1 % (num_1 + num_2) == 0:  # проверяем на деление без остатка
                    password += str(num_1) + str(num_2)  # записываем результат
    print(password)


key()


def key1():
    password = ''
    ar1 = random.randint(3, 20)  # создаем случайное число
    print(ar1)
    for num_1 in range(1, ar1):  # перебираем первое число пары
        for num_2 in range(num_1, ar1):  # перебираем второе число пары
            if ar1 % (num_1 + num_2) == 0:  # проверяем на деление без остатка
                password += str(num_1) + str(num_2)  # записываем результат
    print(password)


key1()
