import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['141589\n', '93261\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([141589, 93261])


if __name__ == '__main__':
    unittest.main()
