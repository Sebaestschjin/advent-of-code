import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day06(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]), is_(17))

    def test_b(self):
        pass


if __name__ == '__main__':
    unittest.main()
