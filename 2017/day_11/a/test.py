import unittest

import solve

class TestStringMethods(unittest.TestCase):

	def read_solution(self, file):
		with open(file, 'r') as solution_file:
			return int(solution_file.readline())

	def do_test(self, count):
		test_name = 'test_' + str(count)
		test_solution = test_name + '_solution'
		print(test_name)
		self.assertEqual(solve.run(test_name), self.read_solution(test_solution))

	def test_all(self):
		for i in range(4):
			self.do_test(i)

if __name__ == '__main__':
    unittest.main()