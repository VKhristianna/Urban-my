import unittest

import tests_12_3 as rt_test



rat_testST = unittest.TestSuite()
rat_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(rt_test.RunnerTest))
rat_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(rt_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)   # Создайте объект класса TextTestRunner, с аргументом verbosity=2

runner.run(rat_testST)
