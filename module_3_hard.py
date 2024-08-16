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

