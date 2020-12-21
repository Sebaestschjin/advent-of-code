import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\n',
                 'trh fvjkl sbzzf mxmxvkd (contains dairy)\n',
                 'sqjhc fvjkl (contains soy)\n',
                 'sqjhc mxmxvkd sbzzf (contains fish)\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
                                         (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
                                         (['sqjhc', 'fvjkl'], ['soy']),
                                         (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])])


if __name__ == '__main__':
    unittest.main()
