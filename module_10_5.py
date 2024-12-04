# Домашнее задание по теме "Многопроцессное программирование"
# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.

import threading
import multiprocessing
import time
from datetime import timedelta


# Создайте функцию read_info(name), где name - название файла.
# Функция должна:
def read_info(name):
    all_data = []                               # 1. Создавать локальный список all_data.
    with open(name, 'r') as file:               # 2. Открывать файл name для чтения.
        while True:
            line = file.readline()              # 3. Считывать информацию построчно (readline),
            if not line:                        # пока считанная строка не окажется пустой.
                break
            all_data.append(line.strip())       # 4. Во время считывания добавлять каждую строку в список all_data.
    return all_data

if __name__ == '__main__':

# 1. Создайте список названий файлов в соответствии с названиями файлов архива.

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# 2. Вызовите функцию read_info для каждого файла по очереди (линейно)
# и измерьте время выполнения и выведите его в консоль.

    start_time = time.time()

    threads = []
    for filename in filenames:
        thread = threading.Thread(target=read_info, args=(filename,))
        threads.append(thread)
        thread.start()                      # Запуск потоков

    for thread in threads:
        thread.join()                       # Завершение потоков

    thread_time = time.time() - start_time
    print(f"{str(timedelta(seconds=thread_time))} - время выполнения потоков.")

# 3. Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
# контекстный менеджер with и объект Pool.
# Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов.
# Измерьте время выполнения и выведите его в консоль.

    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    multiprocessing_time = time.time() - start_time
    print(f"{str(timedelta(seconds=multiprocessing_time))} - время выполнения процессов.")

# Примечания:
# Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
# Выводить или возвращать список all_data в функции не нужно.
# Дополнительно о классе Pool можете прочитать здесь: https://docs.python.org/3/library/multiprocessing.html

# Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
# предварительно закомментировав другой.

# Вывод на консоль, 2 запуска (результаты могут отличаться):
# 0:00:03.046163 (линейный)
# 0:00:01.092300 (многопроцессный)
