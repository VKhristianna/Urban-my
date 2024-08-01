def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # без аргументов
print_params(b=25)  # с изменением только "b"
print_params(c=[1, 2, 3])  # с изменением только "c"

values_list = [9, 'Example', (8, 5)]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

print_params(*values_list)
print_params(**values_dict)

# Исходный код:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
