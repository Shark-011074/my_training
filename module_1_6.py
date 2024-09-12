# СЛОВАРИК
phone_book = {'Denis':88004568888, 'max': 88006664455}
print (phone_book)
print(phone_book['max'])
phone_book['Denis'] = 123456789
print (phone_book)
phone_book['igor'] = 111222333
print (phone_book)
del phone_book ['Denis']
print (phone_book)
phone_book.update({'sasha':789789789,
                   'petr':555566666})
print (phone_book)
print (phone_book.get('maxi','Такого ключа нет'))
phone_book.pop('petr')
print (phone_book)
print()
print (phone_book.keys())
print (phone_book.values())
print (phone_book.items())
print()
phone_book['Denis'] = [123456789, 123, 456, 789]
print (phone_book)

#МНОЖЕСТВО не содержит повторяющихся элементов
set_ = {1,2,3,4,5,2,1,3,4,5,6,'string',True,(1,2,3,4,5)}
print(set_)
print()
print()
print()
#ДОМАШКА



print ('работа со словарем')
my_dict = {'alex':1985, 'tom':1996, 'anna':2005}
print('Словарь my_dict:', my_dict)
print('Значение по ключу "anna":', my_dict['anna'])
print('Значение по отсутствующему ключу:', my_dict.get('petya'))
my_dict.update({'sasha':2004,
                'petr' :2010})
data = my_dict['anna']
print (data)
del my_dict['anna']
print('Измененный словарь :', my_dict)
print()


print('работа с множеством')
my_set = {1,2,3,4,8,5,2,1,3,4,5,6,'string',True,(1,2,3,4,5),True,'string1',6,4,2,8 }
print(my_set)
my_set.add(888) #добавляем int, str,кортеж
my_set.add('add_888')
my_set.add((999, 555, 666))
my_set.remove('string1') #удаляем int, str,кортеж
my_set.remove((1, 2, 3, 4, 5))
my_set.discard(123456)#  discard не сигналит об ошибке при отсутсвии элемента
print(my_set)

'''vyjujcnhjx
ysq  rjvvtynfhbq'''

print("работа со словарем")
my_dict = {'alex': 1985, 'tom': 1996, 'anna': 2005}
print('Словарь my_dict:', my_dict)
print('Значение по ключу "anna":', my_dict['anna'])
print('Значение по отсутствующему ключу:', my_dict.get('petya'))
my_dict.update({'sasha': 2004,
                'petr': 2010})
data = my_dict.pop('anna')
print(data)
print('Измененный словарь :', my_dict)
print()

print('работа с множеством')
my_set = {1, 2, 3, 4, 8, 5, 2, 1, 3, 4, 5, 6, 'string', True, (1, 2, 3, 4, 5), True, 'string1', 6, 4, 2, 8}
print(my_set)
my_set.add(888)
my_set.add('add_888')
my_set.remove('string1')
print(my_set)
