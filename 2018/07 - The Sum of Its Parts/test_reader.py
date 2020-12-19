import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['Step C must be finished before step A can begin.\n',
                 'Step C must be finished before step F can begin.\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([('C', 'A'), ('C', 'F')])


if __name__ == '__main__':
    unittest.main()
