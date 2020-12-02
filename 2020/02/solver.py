def is_valid_a(password, letter, min, max):
    count = password.count(letter)
    return count >= min and count <= max


def solve_a(puzzle):
    valid = 0
    for (letter, min, max, password) in puzzle:
        if is_valid_a(password, letter, min, max):
            valid += 1
    return valid


def is_valid_b(password, letter, first, second):
    return (password[first-1] == letter and password[second-1] != letter) or (password[first-1] != letter and password[second-1] == letter)


def solve_b(puzzle):
    valid = 0
    for (letter, first, second, password) in puzzle:
        if is_valid_b(password, letter, first, second):
            valid += 1
    return valid


def read():
    with open('in', 'r') as file:
        return [split_line(line) for line in file.readlines()]


def split_line(line):
    policy, password = line.split(': ')
    times, letter = policy.split(' ')
    min, max = times.split('-')
    return (letter, int(min), int(max), password)


def run():
    puzzle = read()

    solution_a = solve_a(puzzle)
    print(solution_a)

    solution_b = solve_b(puzzle)
    print(solution_b)


if __name__ == '__main__':
    run()
