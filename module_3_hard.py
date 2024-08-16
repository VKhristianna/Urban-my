def calculate_structure_sum(*args):
    total = 0
    for item in args:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, (list, tuple, set)):
            total += calculate_structure_sum(*item)
        elif isinstance(item, dict):
            total += calculate_structure_sum(*item.keys(), *item.values())
    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(*data_structure)

print(result)

# ==========================================
# def calculate_structure_sum(*args):
#     total_sum = 0
#     total_strings = 0
#
#     for element in args:
#         if isinstance(element, int):  # Проверяем, является ли элемент числом
#             total_sum += element
#         elif isinstance(element, str):  # Проверяем, является ли элемент строкой
#             total_strings += len(element)
#         elif isinstance(element, (list, tuple, set)):  # Если элемент коллекция
#             total_sum += calculate_structure_sum(*element)
#         elif isinstance(element, dict):  # Если элемент словарь
#             for key, value in element.items():
#                 total_sum += calculate_structure_sum([key, value])  # Считаем ключи и значения
#
#     # Возвращаем итоговый результат
#     return total_sum + total_strings
#
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result) 
