from pathlib import Path

from year2021.day04.Board import BingoBoard


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    numbers = [int(line) for line in lines[0].split(",")]

    board_count = (len(lines) - 1) // 6

    boards = []
    for i in range(board_count):
        start = i * 6
        rows = lines[start + 2:start + 7]
        rows = [[int(col) for col in r.strip().split()] for r in rows]
        boards.append(BingoBoard(rows))

    return numbers, boards
