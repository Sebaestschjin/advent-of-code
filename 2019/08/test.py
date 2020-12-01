import unittest
from hamcrest import assert_that, is_

import task_a
import task_b


class Day08(unittest.TestCase):

    def test_a(self):
        assert_that(task_a.solve([1,2,3,4,5,6,7,8,9,0,1,2], 3, 2),
                    is_(1))

    def test_b(self):
        pass

if __name__ == '__main__':
    unittest.main()
