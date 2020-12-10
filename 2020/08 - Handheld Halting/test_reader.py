import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['nop +0\n', 'acc +1\n', 'jmp +4\n', 'acc +3\n', 'jmp -3\n', 'acc -99\n', 'acc +1\n', 'jmp -4\n',
                 'acc +6\n', ]
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3), ('jmp', -3),
                                         ('acc', -99), ('acc', 1), ('jmp', -4), ('acc', 6)])


if __name__ == '__main__':
    unittest.main()
