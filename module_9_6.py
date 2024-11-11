# Домашнее задание по теме "Генераторы"

# Напишите функцию-генератор all_variants(text), которая принимает строку "text" и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
def all_variants(text):
    for _ in range(1, len(text) + 1):
        for start in range(len(text) - _ + 1):   # начальный индекс
            yield text[start:start + _]

# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc


