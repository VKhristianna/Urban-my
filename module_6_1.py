# Задача "Съедобное, несъедобное":
# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность),
# name - индивидуальное название каждого растения
# 4 класса наследника:
# Mammal, Predator для Animal.
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
# Пункты задачи:
# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.
# Создайте объекты этих классов.

"""
Животные - Animal, Родительский класс
"""

class Animal:

    def __init__(self, name):
        self.name = name            # name - индивидуальное название каждого животного.
        self.alive = True           # alive = True(живой)
        self.fed = False            # fed = False(накормленный)

    def eat(self, food):            # метод, где food - параметр, принимающий объекты классов растений.
        if food.edible:             # Если переданное растение (food) съедобное
            print(f"{self.name} съел {food.name}")  # выводит на экран "<self.name> съел <food.name>"
            self.fed = True         # меняется атрибут fed на True.
        else:                       # Если переданное растение (food) не съедобное
            print(f"{self.name} не стал есть {food.name}")  # выводит на экран "<self.name> не стал есть <food.name>"
            self.alive = False      # меняется атрибут alive на False.


"""
Растения - Plant, Родительский класс
"""

class Plant:
    def __init__(self, name):
        self.name = name            # name - индивидуальное название каждого растения
        self.edible = False         # edible = False(съедобность)

"""
Животные, Mammal - млекопитающее - наследник Animal
"""

class Mammal(Animal):
    pass                            # Наследует метод eat от Animal

"""
Животные, Predator - хищник - наследник Animal
"""

class Predator(Animal):
    pass                            # Наследует метод eat от Animal

    """
Растения, Flower - цветок - наследник Plant
"""

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

    """
Растения, Fruit - фрукт - наследник Plant
У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
"""

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Вывод на консоль:
# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True