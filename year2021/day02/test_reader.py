from assertpy import assert_that
import pytest

import year2021.day02.reader as reader


def test_example():
    lines = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([(5, 0), (0, 5), (8, 0), (0, -3), (0, 8), (2, 0)])


@pytest.mark.parametrize('line, expected',
                         [("forward 1", (1, 0)),
                          ("forward 3", (3, 0)),
                          ("up 3", (0, -3)),
                          ("down 1", (0, 1)),
                          ])
def test_parse_line(line, expected):
    result = reader.parse_line(line)
    assert_that(result).is_equal_to(expected)


@pytest.mark.parametrize('line',
                         ["foward 1", "backwards 2",
                          ])
def test_parse_line_invalid(line):
    with pytest.raises(ValueError):
        reader.parse_line(line)
