def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(33, 44, 55)
print_params(7)
print_params(7, 'string')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ('строка', [1, 2, 3], (11, 22, 33))
# print (values_list)
values_dict = {'a': False, 'b': [100, 200, 300], 'c': 400}
# print (values_dict)

print_params(*values_list)
print_params(**values_dict)

value_list2 = (54.52, 'СТРОКА')
print_params(*value_list2, 42)
print('=============================================')
# доп материалы

print('Доп мат 1')
def test_func(*params):
    print("Тип:", type(params))
    print("Аргумент:", params)
test_func(1, 2, 3, 4)
print('=============================================')

print('Доп мат 2')
def summator(txt, *values, type="sum"):
    s = 0
    for i in values:
        print(i)
        s += i
    return f'{txt}{s} {type}'
print(summator("Сумма чисел: ", 22, 33, 44, type="summator"))
print('=============================================')

print('Доп мат 3')
def info(value, *types, names_author="Den", **values):
    print("Тип:", type(values))
    print("Аргумент:", values)
    for key, value in values.items():
        print(key, value)
    print(types)


info("Пример использования параметров всех типов", 2, 3, 4, names_author="Denis", name="Den", course="Python")
print('=============================================')

print('Доп мат 4')
def my_sum(n, *args, txt="Сумма чисел"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)
my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")