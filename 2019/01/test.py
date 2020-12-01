import unittest
from hamcrest import assert_that, is_

import task_a
import task_b


class Day01(unittest.TestCase):

    def test_a(self):
        assert_that(task_a.solve([12]), is_(2))
        assert_that(task_a.solve([14]), is_(2))
        assert_that(task_a.solve([1969]), is_(654))
        assert_that(task_a.solve([100756]), is_(33583))

    def test_b(self):
        assert_that(task_b.solve([12]), is_(2))
        assert_that(task_b.solve([1969]), is_(966))
        assert_that(task_b.solve([100756]), is_(50346))


if __name__ == '__main__':
    unittest.main()
