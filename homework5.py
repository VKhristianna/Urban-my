immutable_var = 'red', 'yellow', 'green', 11, 22, 33 # Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
print(immutable_var) # Выполните операции вывода кортежа immutable_var на экран.
print('Кортеж не поддерживает изменения по элементам:',"immutable_var[0] = 'r'") # Попытайтесь изменить элементы кортежа immutable_var.
print('Поэтому выдает ошибку:','print(immutable_var)') # Объясните, почему нельзя изменить значения элементов кортежа.
mutable_list = ['badminton','tennis','curling',12,23,34,'b','t','c'] # Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
print(mutable_list)
mutable_list[7] = 'tourist' # Измените элементы списка mutable_list.
mutable_list.remove('c')
mutable_list.append('clone')
mutable_list[0] = 1,'badminton'
print(mutable_list) # Выведите на экран измененный список mutable_list.
