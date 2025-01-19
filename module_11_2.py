# Домашнее задание по теме "Интроспекция"
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его (type) тип, атрибуты, методы, модуль, и другие свойства.


import inspect


class Intro:
    def __init__(self):
        self.meaning = 123

    def simple_method(self, value):
        self.meaning = value
        return self.meaning

# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
    # - Тип объекта.
    # - Атрибуты объекта.
    # - Методы объекта.
    # - Модуль, к которому объект принадлежит.
def introspection_info(obj):
    obj_info = {'type': type(obj),
                'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
                'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
                'module': obj.__module__}

# - Другие интересные свойства объекта, учитывая его тип (по желанию).
    if hasattr(obj, '__dict__'):
        obj_info['properties'] = obj.__dict__

    return obj_info

my_object = Intro()
object_info = introspection_info(my_object)

print(object_info)


# Рекомендуется создавать свой класс и объект для лучшего понимания

