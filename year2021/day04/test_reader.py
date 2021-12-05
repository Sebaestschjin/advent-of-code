from assertpy import assert_that

import year2021.day04.reader as reader
from year2021.day04.Board import BingoBoard


def test_example():
    lines = [
        "7,4,9,5,11,17,23,2\n",
        "\n",
        "22 13 17 11  0\n",
        " 8  2 23  4 24\n",
        "21  9 14 16  7\n",
        " 6 10  3 18  5\n",
        " 1 12 20 15 19\n",
        "\n",
        "3 15  0  2 22\n",
        " 9 18 13 17  5\n",
        "19  8  7 25 23\n",
        "20 11 10 24  4\n",
        "14 21 16 12  6\n",
    ]
    numbers, boards = reader.read_lines(lines)
    assert_that(numbers).is_equal_to([7, 4, 9, 5, 11, 17, 23, 2])
    assert_that(boards).is_length(2)

    first_board = BingoBoard([[22, 13, 17, 11, 0],
                              [8, 2, 23, 4, 24],
                              [21, 9, 14, 16, 7],
                              [6, 10, 3, 18, 5],
                              [1, 12, 20, 15, 19]])
    second_board = BingoBoard([[3, 15, 0, 2, 22],
                               [9, 18, 13, 17, 5],
                               [19, 8, 7, 25, 23],
                               [20, 11, 10, 24, 4],
                               [14, 21, 16, 12, 6]])
    assert_that(boards[0]).is_equal_to(first_board)
    assert_that(boards[1]).is_equal_to(second_board)
