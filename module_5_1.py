class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):   # Едем с первого этажа до нового
                print(floor, end='')                # Выводим этажи
                print()                             # С новой строки

# Исходные данные:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"
