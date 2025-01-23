"""Домашнее задание по теме 'Простые Юнит-Тесты'"""

import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        movement = runner.Runner('walk')    # Используем runner.Runner для создания экземпляра
        for _ in range(10):                 # Вызываем метод walk у объекта 10 раз.
            movement.walk()
        self.assertEqual(movement.distance, 50)

    def test_run(self):
        movement = runner.Runner('run')
        for _ in range(10):
            movement.run()
        self.assertEqual(movement.distance, 100)

    def test_challenge(self):
        movement1 = runner.Runner('run2')
        movement2 = runner.Runner('walk2')

        for _ in range(10):                 # У созданных объектов 10 раз вызываются методы run и walk.
            movement1.run()
            movement2.walk()
                                            # Убеждаемся в неравенстве результатов.
        self.assertNotEqual(movement1.distance, movement2.distance)


if __name__ == "__main__":
    unittest.main()


# Вывод на консоль:
# Ran 3 tests in 0.001s OK
