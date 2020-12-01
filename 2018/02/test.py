import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day02(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]), is_(12))

    def test_b(self):
        assert_that(solve_b.run(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]), is_("fgij"))


if __name__ == '__main__':
    unittest.main()
