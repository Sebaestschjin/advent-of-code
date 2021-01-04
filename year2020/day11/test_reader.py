from assertpy import assert_that

import year2020.day11.reader as reader


def test_example():
    lines = ['L.LL.\n', 'LLLLL\n', 'L.L.L\n', 'LLLL.\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to({
        (0, 0): 'L', (1, 0): '.', (2, 0): 'L', (3, 0): 'L', (4, 0): '.',
        (0, 1): 'L', (1, 1): 'L', (2, 1): 'L', (3, 1): 'L', (4, 1): 'L',
        (0, 2): 'L', (1, 2): '.', (2, 2): 'L', (3, 2): '.', (4, 2): 'L',
        (0, 3): 'L', (1, 3): 'L', (2, 3): 'L', (3, 3): 'L', (4, 3): '.',
    })
