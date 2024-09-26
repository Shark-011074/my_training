def get_multiplied_digits(number):
    if number % 10 == 0:
        number = int(number / 10)
    str_number = str(number)
    first = int(str_number[0])
    # print(first)
    if len(str_number) == 1:
        return first
    first = first * get_multiplied_digits(int(str_number[1:]))

    return (first)


print(get_multiplied_digits(40203))
