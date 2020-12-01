import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day05(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run('a'), is_(1))
        assert_that(solve_a.run('aA'), is_(0))
        assert_that(solve_a.run('abBA'), is_(0))
        assert_that(solve_a.run('abAB'), is_(4))
        assert_that(solve_a.run('aabAAB'), is_(6))
        assert_that(solve_a.run('dabAcCaCBAcCcaDA'), is_(10))

    def test_b(self):
        assert_that(solve_b.run("dabAcCaCBAcCcaDA"), is_(4))


if __name__ == '__main__':
    unittest.main()
