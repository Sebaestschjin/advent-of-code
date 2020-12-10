import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['35\n', '20\n', '15\n', '25\n', '47\n', '40\n', '62\n', '55\n', '65\n', '95\n', '102\n', '117\n',
                 '150\n', '182\n', '127\n', '219\n', '299\n', '277\n', '309\n', '576\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277,
                                         309, 576])


if __name__ == '__main__':
    unittest.main()
