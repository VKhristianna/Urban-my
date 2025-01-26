""" Домашнее задание по теме "Систематизация и пропуск тестов". """

import unittest
import runner
import runner_and_tournament as rat


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        movement = runner.Runner('walk')
        for _ in range(10):
            movement.walk()
        self.assertEqual(movement.distance, 50)

    @unittest.skipUnless(True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        movement = runner.Runner('run')
        for _ in range(10):
            movement.run()
        self.assertEqual(movement.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        movement1 = runner.Runner('run2')
        movement2 = runner.Runner('walk2')

        for _ in range(10):
            movement1.run()
            movement2.walk()
        self.assertNotEqual(movement1.distance, movement2.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.name_usain = rat.Runner("Усэйн", 10)
        self.name_andrey = rat.Runner("Андрей", 9)
        self.name_nik = rat.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            result = {place: str(participant) for place, participant in result.items()}
            print(result)

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_race_usain_nik(self):
        tournament = rat.Tournament(90, self.name_usain, self.name_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_nik(self):
        tournament = rat.Tournament(90,self.name_andrey, self.name_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_race_usain_andrey_nik(self):
        tournament = rat.Tournament(90, self.name_usain, self.name_andrey, self.name_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(list(results.values())[-1].name == 'Ник')


if __name__ == "__main__":
    unittest.main()