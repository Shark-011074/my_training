# >>>>>> РАБОТА С УРОКА

# from module_1_5 import list__5
#
# while 1 > 0: # True
#     num =int(input('Введите число: '))
#     if num % 2 == 0:
#         print('Число четное!')
#         continue
#     else:
#         print('Число не четное')
#         break
# print('Я за циклом ')
#
# >>>>>> КОНЕЦ РАБОТЫ С УРОКА

# >>>>>>  ДОМАШНЯЯ РАБОТА

list_1 = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
list_length = len(list_1)
while index < list_length:
    if list_1[index] > 0:
        print(list_1[index])
        index += 1
    elif list_1[index] < 0:
        break
    else:
        index += 1
        continue

# >>>>>>  КОНЕЦ ДОМАШНЕЙ РАБОТЫ

# >>>>>> ДОП ПРАКТИКА

# list_1 = [42, 69, 322,'gcr',True, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
# list_length = len(list_1)-1
# while index <= list_length:
#     if type(list_1[list_length]) == int:
#         if list_1[list_length] >= 0:
#             print(list_1[list_length])
#             list_length -= 1
#         else: list_length -= 1
#     else: list_length -= 1

# >>>>>>  КОНЕЦ ДОП ПРАКТИКА


