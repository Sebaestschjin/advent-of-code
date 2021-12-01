from assertpy import assert_that

import year2021.day01.reader as reader


def test_example():
    lines = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([199, 200, 208, 210, 200, 207, 240, 269, 260, 263, ])
