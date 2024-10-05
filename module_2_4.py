# # >>>>>> РАБОТА С УРОКА
#
# for i in 1, 2, 3, 5, 88, 9, 66:
#     print(i)
#
# for li in 'string STRING':
#     print(li)
#
# for list in ['string', 'STRING', 'STriNG']:
#     print(list)
#
# for i in range(1, 11, 2):  # start , stop, step
#     print(i)

#
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i}x{j}={i * j}')
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i, dict_[i])
#
# dict_1 = {'a': 11, 'b': 22, 'c': 33}
# for k, n in dict_1.items():
#     print(k, n)
#
# # >>>>>> КОНЕЦ РАБОТЫ С УРОКА
from operator import length_hint

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> ДОМАШНЯЯ РАБОТА
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Простые числа делятся только на 1 и на самого себя
not_primes = []  # Не простое число, имеет более 2-х делителей
divider = len(numbers)  # максимально возможное количество делителей в целых числах
for num in numbers:
    if num == 1:
        continue
    n = 0
    for i in range(1, divider + 1):
        if i <= num:
            if num % i == 0:
                n += 1
                if n > 2:
                    not_primes.append(num)
                    break
            else:
                continue
        else:
            break
    if n == 2:
        primes.append(num)
print('Primes: ', primes)
print('Not Primes', not_primes)

# >>>>>>  КОНЕЦ ДОМАШНЯЯ РАБОТА


# # >>>>>> ДОМАШНЯЯ РАБОТА РАЗРАБОТКА КОДА
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []  # Простые числа делятся только на 1 и на самого себя
# not_primes = []  # Не простое число, имеет более 2-х делителей
# divider = len(numbers)  # максимально возможное количество делителей в целых числах
#
# for num in numbers:
#     print('Исследуем число ', num)
#     if num == 1:
#         print('1 - число никакое!!!')
#         continue
#     n = 0
#     for i in range(1, divider + 1):
#         if i <= num:
#             print('число ', num, 'делим на ', i)
#             if num % i == 0:
#                 n += 1
#                 print('число разделилось  ', n, 'раз')
#                 if n > 2:
#                     print('обычное число', num)
#                     not_primes.append(num)
#                     break
#             else:
#                 continue
#         else:
#             break
#     if n == 2:
#         print('n делений = ', n, ' простое число', num)
#         primes.append(num)
#
# print('Primes: ', primes)
# print('Not Primes', not_primes)



