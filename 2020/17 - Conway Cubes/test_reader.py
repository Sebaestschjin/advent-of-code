import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['.#.\n', '..#\n', '###\n']
        result = reader.read_lines(lines)

        assert_that(result).is_equal_to({(0, 0): '.', (1, 0): '#', (2, 0): '.',
                                         (0, 1): '.', (1, 1): '.', (2, 1): '#',
                                         (0, 2): '#', (1, 2): '#', (2, 2): '#',
                                         })


if __name__ == '__main__':
    unittest.main()
