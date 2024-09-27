sum_ = 0


def calculate_structure_sum(a):
    global sum_
    for i in a:
        if isinstance(i, int) and type(i) != bool:
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, bool):
            bool_ = str(i)
            sum_ += len(bool_)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            calculate_structure_sum(i)
        elif isinstance(i, dict):
            for j in i:
                if isinstance(i[j], int):
                    sum_ = sum_ + i[j]
                elif isinstance(i[j], str):
                    sum_ = sum_ + len(i[j])
            calculate_structure_sum(i)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print('summa = ', result)
