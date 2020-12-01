import unittest

import solve

class TestStringMethods(unittest.TestCase):

	def __do_test__(self, count, result):
		self.assertEqual(solve.run('test_' + str(count)), result)

	def test_all(self):
		self.__do_test__(1, 6)
		self.__do_test__(2, 0)
		self.__do_test__(3, 4)
		self.__do_test__(4, 12)
		self.__do_test__(5, 4)
		

if __name__ == '__main__':
    unittest.main()