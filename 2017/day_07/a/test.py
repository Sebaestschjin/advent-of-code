import unittest

import solve

class TestStringMethods(unittest.TestCase):

	def read_solution(self, file):
		with open(file, 'r') as solution_file:
			return solution_file.readline()

	def do_test(self, count):
		test_name = 'test_' + str(count)
		test_solution = test_name + '_solution'
		self.assertEqual(solve.run(test_name), self.read_solution(test_solution))

	def test_all(self):
		for i in range(1):
			self.do_test(i)

if __name__ == '__main__':
    unittest.main()