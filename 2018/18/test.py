import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day08(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]),
                    is_(138))

    def test_b(self):
        assert_that(solve_b.run([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]),
                    is_(66))


if __name__ == '__main__':
    unittest.main()
