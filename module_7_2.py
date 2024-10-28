# 1. Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# 2. Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка.

def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:    # Записывает информацию и закрывает файл
        for i in range(len(strings)):
            string = strings[i]
            byte_position = file.tell() # Получаем номера байта начала строки перед записью
            file.write(string + '\n')   # Запись строки в файл + символ новой строки
            strings_positions[(i + 1, byte_position)] = string  # Сохраняем номер строки и байт начала строки в словаре

    return strings_positions

# Пример выполняемого кода:
info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

# Как выглядит файл 'test.txt' после запуска:
# Text for tell.
# Используйте кодировку utf-8.
# Because there are 2 languages!
# Спасибо!

