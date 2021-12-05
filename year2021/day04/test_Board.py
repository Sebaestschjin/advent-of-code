from assertpy import assert_that

from year2021.day04.Board import BingoBoard

example_data = [[14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7]]


def test_get_number():
    example = BingoBoard(example_data)

    assert_that(example.get_number(22)).is_equal_to((3, 0))
    assert_that(example.get_number(20)).is_equal_to((2, 4))
    assert_that(example.get_number(100)).is_none()


def test_get_score():
    example = BingoBoard(example_data)
    example.mark(7)
    example.mark(4)
    example.mark(9)
    example.mark(5)
    example.mark(11)
    example.mark(17)
    example.mark(23)
    example.mark(2)
    example.mark(0)
    example.mark(14)
    example.mark(21)
    example.mark(24)

    result = example.get_score(24)
    assert_that(result).is_equal_to(4512)


def test_is_solved_row():
    example = BingoBoard(example_data)
    assert_that(example.is_solved()).is_false()

    example.mark(10)
    assert_that(example.is_solved()).is_false()
    example.mark(16)
    assert_that(example.is_solved()).is_false()
    example.mark(15)
    assert_that(example.is_solved()).is_false()
    example.mark(9)
    assert_that(example.is_solved()).is_false()
    example.mark(19)
    assert_that(example.is_solved()).is_true()


def test_is_column():
    example = BingoBoard(example_data)
    assert_that(example.is_solved()).is_false()

    example.mark(21)
    assert_that(example.is_solved()).is_false()
    example.mark(16)
    assert_that(example.is_solved()).is_false()
    example.mark(8)
    assert_that(example.is_solved()).is_false()
    example.mark(11)
    assert_that(example.is_solved()).is_false()
    example.mark(0)
    assert_that(example.is_solved()).is_true()
