food =["apple", "coconut","banana"]
print(food[0])
food[0] = "peach"
print(food)
food.append(True)
print(food)
food.append('125ghj')
print(food)
food.extend("string")
print(food)
food.extend(["string", 2, 5, True])
print(food)
food.remove("coconut")
print(food)
print("coconut" in food)
print("coconut" not in food)
print(food[0::2])
print()
print()
print()




print('кортеж')
tuple_1 = 1,2,3,4
tuple_2 = (1,2,3,4)
tuple_3 = tuple([1,2,3,4])
print(type(tuple_1))
print(tuple_1)
print(tuple_2)
print(tuple_3)
print(type(tuple_3))
tuple_4 = 1,2,3,4,True,"string"
print(tuple_4)
print(tuple_4[0::2])

#кортеж не позволяет менять значения, удалять
# print(tuple_4[-1])
# tuple_4.remuve[-1]
# tuple_4[-1] = 200

#кортеж занимает меньше памяти
tuple_5 = 1,2,3,4,True,"string"  #кортеж
list__5 = [1,2,3,4,True,"string"]#список
print(tuple_5.__sizeof__())
print(list__5.__sizeof__())

#кортеж может содержать внутри себя список
tuple_6 = ([1,2,3,4],1,2,3,4)
print(tuple_6)
tuple_6[0][1] = 7
print(tuple_6)
#tuple_6[0][1].remove()#  ?  можно ли удалять и добавлять

tuple_7 = tuple_1 + tuple_6
print(tuple_7)

tuple_8 = tuple_1 * 4
print(tuple_8)

print()
print()
print()
print()
print()



immutable_var = (11,12,"coconut",True,24.54)
print(immutable_var)
#immutable_var[0]
mutable_list = [11,12,"coconut",True,24.54]
mutable_list[0] = "apple"
mutable_list[1] = 112
mutable_list[2] = False
mutable_list.remove(24.54)
mutable_list.append("add")
print(mutable_list)
# пробные
print()
print()
mutable_list = mutable_list *2
print(mutable_list)
mutable_list[0] = "!@#$%^&*()"
print(mutable_list)
mutable_list[4] = "!@#$%^&*()"
print(mutable_list)
mutable_list[4:1] = "!@#$%^&*()"
print(mutable_list)
mutable_list[4::] = "!@#$%^&*()"
print(mutable_list)



