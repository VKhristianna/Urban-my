# Домашнее задание по теме "Введение в потоки".
# Задача "Потоковая запись в файлы":

import threading
from time import sleep, time

# Необходимо создать функцию write_words(word_count, file_name),
# где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
# после записи каждого на 0.1 секунды.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

def write_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as file:

        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time()

# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f'Время выполнения функции {end_time - start_time:.6f} секунд(ы)')

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
threads = []
start_time_threads = time()

threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

# Запустите эти потоки методом start
for thread in threads:
    thread.start()

# не забыв, сделать остановку основного потока при помощи join.
for thread in threads:
    thread.join()

end_time_threads = time()
# Также измерьте время затраченное на выполнение функций и потоков.
print(f'Время выполнения потоков {end_time_threads - start_time_threads:.6f} секунд(ы)')


# Вывод на консоль:

# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411             # Может быть другое время (34.151126)
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575             # Может быть другое время (20.087140)
