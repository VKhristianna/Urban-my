# Домашнее задание по теме "Файлы в операционной системе".

import os
import time

directory = "."     # Задаём текущую директорию
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
for root, dirs, files in os.walk(directory):
    for file in files:
# Примените os.path.join для формирования полного пути к файлам.
        filepath = os.path.join(root, file)
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

# Используйте os.path.getsize для получения размера файла.
        filesize = os.path.getsize(filepath)
# Используйте os.path.dirname для получения родительской директории файла.
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

