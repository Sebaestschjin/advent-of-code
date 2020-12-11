import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['L.LL.LL.LL\n', 'LLLLLLL.LL\n', 'L.L.L..L..\n', 'LLLL.LL.LL\n', 'L.LL.LL.LL\n', 'L.LLLLL.LL\n',
                 '..L.L.....\n', 'LLLLLLLLLL\n', 'L.LLLLLL.L\n', 'L.LLLLL.LL\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to(['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL',
                                         'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL', ])


if __name__ == '__main__':
    unittest.main()
