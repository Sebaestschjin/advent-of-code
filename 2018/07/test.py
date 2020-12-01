import unittest
from hamcrest import assert_that, is_

import solve_a
import solve_b


class Day06(unittest.TestCase):

    def test_a(self):
        assert_that(solve_a.run(['Step C must be finished before step A can begin.',
                                 'Step C must be finished before step F can begin.',
                                 'Step A must be finished before step B can begin.',
                                 'Step A must be finished before step D can begin.',
                                 'Step B must be finished before step E can begin.',
                                 'Step D must be finished before step E can begin.',
                                 'Step F must be finished before step E can begin.']),
                    is_('CABDFE'))

    def test_b(self):
        assert_that(solve_b.run(['Step C must be finished before step A can begin.',
                                 'Step C must be finished before step F can begin.',
                                 'Step A must be finished before step B can begin.',
                                 'Step A must be finished before step D can begin.',
                                 'Step B must be finished before step E can begin.',
                                 'Step D must be finished before step E can begin.',
                                 'Step F must be finished before step E can begin.']),
                    is_(15))


if __name__ == '__main__':
    unittest.main()
