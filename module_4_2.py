# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function,
# Эта функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()  # Вызов функции inner_function внутри test_function


test_function()  # Вызов функции test_function

# Вызвать inner_function вне функции test_function невозможно, так как она недоступна вне test_function,
# то есть вне своей области видимости.
