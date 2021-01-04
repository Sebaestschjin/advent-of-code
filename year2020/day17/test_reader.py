from assertpy import assert_that

import year2020.day17.reader as reader


def test_example():
    lines = ['.#.\n', '..#\n', '###\n']
    result = reader.read_lines(lines)

    assert_that(result).is_equal_to({(0, 0): '.', (1, 0): '#', (2, 0): '.',
                                     (0, 1): '.', (1, 1): '.', (2, 1): '#',
                                     (0, 2): '#', (1, 2): '#', (2, 2): '#',
                                     })
