# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Цель: Применить очереди в работе с потоками, используя класс Queue.
# Задача "Потоки гостей в кафе":

from threading import Thread
from queue import Queue
from random import randint
import time

# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
# 1. Объекты этого класса должны создаваться следующим способом - Table(1)
# 2. Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
class Table:
    def __init__(self, number):
        self.number = number        # Номер стола
        self.guest = None           # Гость за столом (по умолчанию None)

# Класс Guest:
# 1. Должен наследоваться от класса Thread (быть потоком).
# 2. Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# 3. Обладать атрибутом name - имя гостя.
class Guest(Thread):
    def __init__(self, name):
        super().__init__()          # Инициализация потока
        self.name = name            # Имя гостя
# 4. Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
    def run(self):
        time.sleep = randint(3, 10)

# Класс Cafe:
# 1. Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# 2. Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

# 3. Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
# 1. Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# 2. Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя
# и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
    def guest_arrival(self, *guests):
        for guest in guests:
            place = False                       # Отслеживаем размещения гостя
            for table in self.tables:           # Проверяем наличие свободного стола
                if table.guest is None:         # Для проверки значения на None используйте оператор is (table.guest is None)
                    table.guest = guest         # Помещаем гостя за стол
                    guest.start()               # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    place = True                # Гость успешно размещен
                    break
# 3. Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue
# и выводить сообщение "<имя гостя> в очереди".
            if not place:                       # Если все столы заняты
                self.queue.put(guest)           # Добавляем гостя в очередь
                print(f"{guest.name} в очереди")

# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# 1. Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# 2. Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
# то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
# Так же текущий стол освобождается (table.guest = None).
# 3. Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается
# гость взятый из очереди (queue.get()).
# 4. Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
# Далее запустить поток этого гостя (start)

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:                 # Проверка, занят ли стол
                    if not table.guest.is_alive():          # Если гость поел
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None                  # Освобождается стол
                        if not self.queue.empty():          # Проверяем очередь
                            next_guest = self.queue.get()   # Берем следующего гостя из очереди
                            table.guest = next_guest        # Сажаем следующего гостя за стол
                            next_guest.start()              # Запускаем поток этого гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

# Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
# .....
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
