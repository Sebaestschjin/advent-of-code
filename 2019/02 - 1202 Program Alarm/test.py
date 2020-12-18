import unittest
from hamcrest import assert_that, is_

import task_a
import task_b


class Day02(unittest.TestCase):

    def test_a(self):
        assert_that(task_a.solve([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50, 60]),
                    is_(3100))

    def test_b(self):
        pass


if __name__ == '__main__':
    unittest.main()
