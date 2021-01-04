from assertpy import assert_that

import year2020.day19.reader as reader


def test_example():
    lines = ['0: 1 2\n', '1: "a"\n', '2: 1 3 | 3 1\n', '3: "b"\n', '\n', 'aab\n', 'aba\n', 'abaa\n']
    rules, words = reader.read_lines(lines)
    assert_that(rules).is_equal_to({0: [1, 2], 1: 'a', 2: [[1, 3], [3, 1]], 3: 'b'})
    assert_that(words).is_equal_to(['aab', 'aba', 'abaa'])
