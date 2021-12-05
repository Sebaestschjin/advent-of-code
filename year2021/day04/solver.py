from typing import List, Tuple

from year2021.day04.Board import BingoBoard


def solve_boards(numbers: List[int], boards: List[BingoBoard]):
    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.is_solved():
                return board.get_score(number)


def solve_a(puzzle: Tuple[List[int], List[BingoBoard]]):
    numbers, boards = puzzle

    return solve_boards(numbers, boards)


def solve_b(puzzle: Tuple[List[int], List[BingoBoard]]):
    numbers, boards = puzzle

    for number in numbers:
        for board in boards:
            board.mark(number)

        boards = [board for board in boards if not board.is_solved()]

        if len(boards) == 1:
            return solve_boards(numbers, boards)
