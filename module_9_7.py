# Домашнее задание по теме "Декораторы"

# Напишите 2 функции:
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.

# Примечания:
# 1. Не забудьте написать внутреннюю функцию wrapper в is_prime
# 2. Функция is_prime должна возвращать wrapper
# 3. @is_prime - декоратор для функции sum_three

def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i != 0:
                    print("Простое")
                return result

    return wrapper


@is_prime
def sum_three(a, b, c):         # Функция, которая складывает 3 числа (sum_three)
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11




