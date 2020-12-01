import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day01(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run([1, 1, 1]), is_(3))
        assert_that(solve_a.run([1, 1, -2]), is_(0))
        assert_that(solve_a.run([-1, -2, -3]), is_(-6))

    def test_b(self):
        assert_that(solve_b.run([1, -1]), is_(0))
        assert_that(solve_b.run([3, 3, 4, -2, -4]), is_(10))
        assert_that(solve_b.run([-6, 3, 8, 5, -6]), is_(5))
        assert_that(solve_b.run([7, 7, -2, -7, -4]), is_(14))


if __name__ == '__main__':
    unittest.main()
