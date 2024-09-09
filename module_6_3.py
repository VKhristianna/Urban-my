# Задача "Мифическое наследование":

"""
Horse - класс описывающий лошадь
"""
class Horse:
    sound = 'Frrr'              # sound = 'Frrr' - звук, который издаёт лошадь.
    def __init__(self):
        self.x_distance = 0     # x_distance = 0 - пройденный путь

    def run(self, dx):
        self.x_distance += dx   # run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

"""
Eagle - класс описывающий орла
"""
class Eagle:
    sound = 'I train, eat, sleep, and repeat'   # sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
    def __init__(self):
        self.y_distance = 0     # y_distance = 0 - высота полёта

    def fly(self, dy):
        self.y_distance += dy   # fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

"""
Pegasus - класс описывающий пегаса
"""
class Pegasus(Horse, Eagle):    # Наследуется от Horse и Eagle
    sound = Eagle.sound
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self,dx, dy):      # move(self, dx, dy) - где dx и dy изменения дистанции.
        self.run(dx)
        self.fly(dy)

    def get_pos(self):                           # get_pos(self) возвращает текущее положение пегаса
        return self.x_distance, self.y_distance  # в виде кортежа  - (x_distance, y_distance)

    def voice(self):                            # 3. voice - который печатает значение унаследованного атрибута sound.
        print(self.sound)

# Пример работы программы:
p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()

# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat