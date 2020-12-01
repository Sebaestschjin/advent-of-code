import unittest
from hamcrest import assert_that, is_

import task_a
import task_b


class Day06(unittest.TestCase):

    def test_a(self):
        assert_that(task_a.solve([['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L']]),
                    is_(42))

    def test_b(self):
        assert_that(task_b.solve([['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L'], ['K', 'YOU'], ['I', 'SAN']]),
                    is_(4))


if __name__ == '__main__':
    unittest.main()
