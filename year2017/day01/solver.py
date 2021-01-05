import year2017.day01.reader as reader


def find_applicable_a(numbers):
    offset = 1
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i + offset) % len(numbers)]:
            yield numbers[i]


def find_applicable_b(numbers):
    offset = int(len(numbers) / 2)
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i + offset) % len(numbers)]:
            yield numbers[i]


def solve_a(numbers):
    return sum(find_applicable_a(numbers))


def solve_b(numbers):
    return sum(find_applicable_b(numbers))


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
