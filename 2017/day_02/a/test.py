import unittest

import solve

class TestStringMethods(unittest.TestCase):

	def __do_test__(self, count, result):
		self.assertEqual(solve.run('test_' + str(count)), result)

	def test_all(self):
		self.__do_test__(1, 18)

if __name__ == '__main__':
    unittest.main()