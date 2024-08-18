# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.

def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second


# result1 = divide(69, 3)
# result2 = divide(3, 0)
#
# print(result1)
# print(result2)
