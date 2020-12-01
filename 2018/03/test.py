import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day02(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]), is_(4))

    def test_b(self):
        assert_that(solve_b.run(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]), is_(3))


if __name__ == '__main__':
    unittest.main()
