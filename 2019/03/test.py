import unittest
from hamcrest import assert_that, is_

import task_a
import task_b


class Day03(unittest.TestCase):

    def test_a(self):
        assert_that(task_a.solve([['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']]), is_(6))
        assert_that(task_a.solve([['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                                  ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]),
                                  is_(159))
        assert_that(task_a.solve([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
                                  ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]),
                                  is_(135))

    def test_b(self):
        assert_that(task_b.solve([['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']]), is_(30))
        assert_that(task_b.solve([['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                                  ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]),
                                  is_(610))
        assert_that(task_b.solve([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
                                  ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]),
                                  is_(410))


if __name__ == '__main__':
    unittest.main()
