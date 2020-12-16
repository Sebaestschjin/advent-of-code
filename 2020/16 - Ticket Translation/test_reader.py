import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['class: 1-3 or 5-7\n', 'row: 6-11 or 33-44\n', 'seat: 13-40 or 45-50\n', '\n', 'your ticket:\n',
                 '7,1,14\n', '\n', 'nearby tickets:\n', '7,3,47\n', '40,4,50\n', '55,2,20\n', '38,6,12\n']

        rules, tickets = reader.read_lines(lines)
        assert_that(rules).is_equal_to({'class': ((1, 3), (5, 7)), 'row': ((6, 11), (33, 44)),
                                        'seat': ((13, 40), (45, 50))})

        assert_that(tickets).is_equal_to([[7, 1, 14], [7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]])


if __name__ == '__main__':
    unittest.main()
