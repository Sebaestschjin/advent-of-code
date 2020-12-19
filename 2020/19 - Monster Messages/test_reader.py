import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['0: 1 2\n', '1: "a"\n', '2: 1 3 | 3 1\n', '3: "b"\n', '\n', 'aab\n', 'aba\n', 'abaa\n']
        rules, words = reader.read_lines(lines)
        assert_that(rules).is_equal_to({0: [1, 2], 1: 'a', 2: [[1, 3], [3, 1]], 3: 'b'})
        assert_that(words).is_equal_to(['aab', 'aba', 'abaa'])


if __name__ == '__main__':
    unittest.main()
