
num_1 = int(input('Введите первое число '))
num_2 = int(input('Введите второе число '))
num_3 = int(input('Введите третье число '))
# print(num_1)
# print(num_2)
# print(num_3)
if num_1 == num_2 and num_1 == num_3:
    print('3')
elif ((num_1 == num_2 and num_1 != num_3) or
      (num_2 == num_3 and not num_2 == num_1) or
      (num_3 == num_1 and not num_3 == num_2)):
    print('2')
else:
    print('0')

