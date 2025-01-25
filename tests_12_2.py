""" Домашнее задание по теме "Методы Юнит-тестирования" """

import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.name_usain = rat.Runner("Усэйн", 10)
        self.name_andrey = rat.Runner("Андрей", 9)
        self.name_nik = rat.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):         # метод, где выводятся all_results по очереди в столбец.
        for result in cls.all_results.values():
            result = {place: str(participant) for place, participant in result.items()}
            print(result)

    """ 
Тестирование трёх забегов. Участвуют (порядок передачи в объект Tournament соблюсти):
1. Усэйн и Ник; 2. Андрей и Ник; 3. Усэйн, Андрей и Ник.
Ник всегда должен быть последним. 
"""

    def test_race_usain_nik(self):
        tournament = rat.Tournament(90, self.name_usain, self.name_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')   # сравнивается последний объект из all_results
                                                                    # и предполагаемое имя последнего бегуна.

    def test_race_andrey_nik(self):
        tournament = rat.Tournament(90,self.name_andrey, self.name_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')

    def test_race_usain_andrey_nik(self):
        tournament = rat.Tournament(90, self.name_usain, self.name_andrey, self.name_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')


if __name__ == "__main__":
    unittest.main()

# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}

# Ran 3 tests in 0.001s OK

