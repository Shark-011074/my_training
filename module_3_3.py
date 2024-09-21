def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params(33,44,55)
print_params(7)
print_params(7,'string')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list =('строка',[1,2,3],(11,22,33) )
#print (values_list)
values_dict = {'a':False, 'b':[100,200,300],'c':400}
#print (values_dict)

print_params(*values_list)
print_params(**values_dict)

value_list2 = (54.52,'СТРОКА')
print_params(*value_list2,42)