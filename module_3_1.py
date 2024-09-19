import random

calls = 0
number_of_repetitions = int(input('Введите количество повторений - '))
nm = 0
list_ = ['PyThon', 'TuTor', 'desIgnEd', 'TO', 'iMITate', 'wHAt', 'An', 'INstRYctor', 'An', 'OrintROductY',# Набор строк для произвольного выбора в функции №3
         'pROGRamming', 'dRAWs', 'oN', 'tHE', 'bLACKboard']
num_list_ = len(list_)


def count_calls():  # функция счетчик
    global calls
    calls += 1


def string_info(str1):  # функция №2, кортеж строка и регистры
    count_calls()
    tuple_str1 = (len(str1), str1.upper(), str1.lower())
    print(tuple_str1)


def is_contains(string, list_to_search):# Функция №3 прверяет наличие случайной строки в случайном списке и вовращает True/False
    count_calls()
    print(str_2, list_to_search_1)
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return True
    else:
        return False


while nm < number_of_repetitions:
    nm += 1
    str_1 = input('Введите текст - ')  # для функции string_info()
    string_info(str_1)
    list_to_search_1 = []
    str_2 = random.choice(list_)  # для функции is_contains() выбрали случайную строку из  списка
    str_2 = str_2.lower()
    for i in range(round(num_list_ / 3 * 2)):  # создаем случайный набор строк в списке, 66% от общего количества
        list_to_search_1.append(random.choice(list_))
    print(is_contains(str_2, list_to_search_1)) # Вызываем функцию и возвращаем значение)
    # summ = is_contains(str_2, list_to_search_1)
    # print(summ)
    print()
print('Функция "calls" вызывалась ', calls, 'раз(а)')
