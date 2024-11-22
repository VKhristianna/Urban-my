# Домашнее задание по теме "Потоки на классах"
# Задача "За честь и отвагу!":

from threading import Thread
import time

# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)

class Knight(Thread):

    def __init__(self, name, power, delay):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.delay = delay
        self.days = 0
        self.enemies = 100  # На каждого рыцаря по 100 врагов

    def timer(self, name, enemies, delay):

        while enemies:
            time.sleep(delay)
            enemies = 0

# А также метод run, в котором рыцарь будет сражаться с врагами:
# 1. При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# 2. Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# 3. В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# 4. По прошествию 1 дня сражения (1 секунды) выводится строка
# "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# 5. После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.timer(self.name, self.enemies, self.delay)
            self.enemies -= self.power
            self.days += 1
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

# Создаем рыцарей
first_knight = Knight('Sir Lancelot', 10, 0.5)
second_knight = Knight("Sir Galahad", 20, 1)

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ожидаем завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")

# Вывод на консоль:
# Sir Lancelot, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, на нас напали!
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Galahad одержал победу спустя 5 дней(дня)!
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней(дня)!
# Все битвы закончились!
