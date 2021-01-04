from assertpy import assert_that

import year2020.day21.reader as reader


def test_example():
    lines = ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\n',
             'trh fvjkl sbzzf mxmxvkd (contains dairy)\n',
             'sqjhc fvjkl (contains soy)\n',
             'sqjhc mxmxvkd sbzzf (contains fish)\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
                                     (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
                                     (['sqjhc', 'fvjkl'], ['soy']),
                                     (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])])
