# Словари
my_dict = {'Александр': 1990, 'Валентина': 1995, 'Виктор': 1998,'Светлана': 1997} # Словарь: Имя/Год рождения
print(my_dict)
print(my_dict['Виктор']) # Выведите на экран одно значение по существующему ключу
print(my_dict.get('Нина')) # по отсутствующему из словаря my_dict без ошибки.
print(my_dict)
my_dict.update({'Демьян': 2001, 'Юлиана': 1992}) # Добавьте ещё две произвольные пары того же формата в словарь my_dict.
print(my_dict)
a = my_dict.pop('Александр') # - Удалите одну из пар в словаре по существующему ключу из словаря
print(a) # выведите значение из этой пары на экран
print(my_dict)
# Множества
my_set = {11, 22, 33, 44, 55, 33, 11, 'cancer','fish','scorpio','fish',(12,6,3),(3,6,12) } # Создать переменную my_set, присвоить ей множество из разных типов данных с повторяющимися значениями.
print(my_set)
my_set.add('a+b') # Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.update({'k','v'})
print(my_set)
my_set.discard((3, 6, 12)) # Удалите один любой элемент из множества
print(my_set)

