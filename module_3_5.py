def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number)==1:
        return first
    else:
        first = first * get_multiplied_digits(int(str_number[1:]))

    return (first)

print(get_multiplied_digits(40203))

# def print_num(a):
#     print(a)
# print_num(010)