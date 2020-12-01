import unittest
from hamcrest import assert_that, is_

import task_a
import task_b


class Day01(unittest.TestCase):

    def test_a(self):
        # assert_that(task_a.solve([12]), is_(2))
        pass

    def test_b(self):
        # assert_that(task_b.solve([12]), is_(2))
        pass


if __name__ == '__main__':
    unittest.main()
