""" Домашнее задание по теме "Логирование" """

import unittest
import rt_with_exceptions as rtwe
import logging

logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename='runner_tests.log',
                    encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(funcName)s | %(lineno)d | %(message)s')

# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            movement = rtwe.Runner('Walker', -5)            # Передаем отрицательное значение в speed
            logging.info('"test_walk" выполнен успешно')            # Логируем успешное выполнение
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)      # Логируем предупреждение
        else:
            for _ in range(10):
                movement.walk()
            self.assertEqual(movement.distance, 50)

    @unittest.skipUnless(True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            movement = rtwe.Runner(1234, 10)        # Передаем что-то кроме строки в name
            logging.info('"test_run" выполнен успешно')             # Логируем успешное выполнение
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)    # Логируем предупреждение
        else:
            for _ in range(10):
                movement.run()
            self.assertEqual(movement.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        movement1 = rtwe.Runner('run2')
        movement2 = rtwe.Runner('walk2')

        for _ in range(10):
            movement1.run()
            movement2.walk()
        self.assertNotEqual(movement1.distance, movement2.distance)


if __name__ == "__main__":

    unittest.main()



# Файл tests_12_4.py с классами тестов и runner_tests.log с логами тестов загрузите на ваш GitHub репозиторий.

