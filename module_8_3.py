# Домашнее задание по теме "Создание исключений"
# Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи.
# Повторить тему ООП и принцип инкапсуляции.
# Создайте 3 класса (2 из которых будут исключениями):

# Классы исключений IncorrectVinNumber и IncorrectCarNumbers.
# Объекты обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):

        self.model = model            # 1. Атрибут объекта model - название автомобиля (строка).
        self.__vin = vin              # 2. Атрибут объекта __vin - vin номер автомобиля (целое число).
        self.__numbers = numbers      # 4. Атрибут __numbers - номера автомобиля (строка).
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

# Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении
# атрибутов __vin и __numbers).

# __is_valid_vin
# 1. Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число.
# (тип данных можно проверить функцией isinstance).
# 2. Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число
# находится не в диапазоне от 1000000 до 9999999 включительно.
# 3. Возвращает True, если исключения не были выброшены.

    def __is_valid_vin(self, vin_number):

            if not isinstance (vin_number, int):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if not (1000000 <= vin_number <= 9999999):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return True

# __is_valid_numbers
# 1. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
# если передана не строка. (тип данных можно проверить функцией isinstance).
# 2. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять
# ровно из 6 символов.
# 3. Возвращает True, если исключения не были выброшены.

    def __is_valid_numbers(self, numbers):

        if not isinstance (numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

# Пример результата выполнения программы:
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')


try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')


try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

# Вывод на консоль:
# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера

# Примечания:
# Для выбрасывания исключений используйте оператор raise


