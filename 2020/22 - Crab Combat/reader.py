from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    first, second = ''.join(lines).split('\n\n')
    return read_deck(first), read_deck(second)


def read_deck(lines):
    return [int(card) for card in lines.strip().split('\n')[1:]]
