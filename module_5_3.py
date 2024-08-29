class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):  # Проверка, что value число
            return House(self.name, self.number_of_floors + value)
        else:
            return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)                   # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)                   # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # __eq__   # False
h1 = h1 + 10     # __add__
print(h1)                   # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)             # True

h1 += 10    # __iadd__      # Название: ЖК Эльбрус, кол-во этажей: 30
print(h1)

h2 = 10 + h2  # __radd__    # Название: ЖК Акация, кол-во этажей: 30
print(h2)

print(h1 > h2)   # __gt__   # False
print(h1 >= h2)  # __ge__   # True
print(h1 < h2)   # __lt__   # False
print(h1 <= h2)  # __le__   # True
print(h1 != h2)  # __ne__   # False
