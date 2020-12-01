import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day02(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run(['[1518-11-01 00:00] Guard #10 begins shift',
                                 '[1518-11-01 00:05] falls asleep',
                                 '[1518-11-01 00:25] wakes up',
                                 '[1518-11-01 00:30] falls asleep',
                                 '[1518-11-01 00:55] wakes up',
                                 '[1518-11-01 23:58] Guard #99 begins shift',
                                 '[1518-11-02 00:40] falls asleep',
                                 '[1518-11-02 00:50] wakes up',
                                 '[1518-11-03 00:05] Guard #10 begins shift',
                                 '[1518-11-03 00:24] falls asleep',
                                 '[1518-11-03 00:29] wakes up',
                                 '[1518-11-04 00:02] Guard #99 begins shift',
                                 '[1518-11-04 00:36] falls asleep',
                                 '[1518-11-04 00:46] wakes up',
                                 '[1518-11-05 00:03] Guard #99 begins shift',
                                 '[1518-11-05 00:45] falls asleep',
                                 '[1518-11-05 00:55] wakes up']), is_(240))

    def test_b(self):
        assert_that(solve_b.run(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]), is_(3))


if __name__ == '__main__':
    unittest.main()
