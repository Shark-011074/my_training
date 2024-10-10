class House:


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей {self.number_of_floors}'

    def __eq__(self, other):  # True если значение аттрибутов класса равны
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

        elif isinstance(other, int) or isinstance(other, float):
            return self.number_of_floors == other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        elif isinstance(other, int) or isinstance(other, float):
            self.number_of_floors = self.number_of_floors + other
            return self

    def __lt__(self, other):  # True если значение self аттрибута класса меньше
        return self.number_of_floors < other.number_of_floors

    def __iadd__(self, other):
        House.__add__(self, other)
        return self

    def __radd__(self, other):
        House.__add__(self, other)
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
#
print(h1 == h2)  # __eq__
#
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)
#
h1 += 10  # __iadd__
print(h1)
#
h2 = 10 + h2  # __radd__
print(h2)
#
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
