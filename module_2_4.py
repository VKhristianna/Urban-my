# Вывод на консоль:
# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Дано
primes = []     # Список 2
not_primes = [] # Список 3

for number in numbers:
    is_prime = True # Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
    if number > 1:
        for i in range(2, number): # Вложенный цикл for
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        else:
            not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)
