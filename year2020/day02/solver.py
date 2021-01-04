import year2020.day02.reader as reader


def is_valid_a(password, letter, lower, upper):
    count = password.count(letter)
    return lower <= count <= upper


def solve_a(rules):
    valid = 0
    for (letter, lower, upper, password) in rules:
        if is_valid_a(password, letter, lower, upper):
            valid += 1
    return valid


def is_valid_b(password, letter, first, second):
    first_has_letter = password[first-1] == letter
    second_has_letter = password[second-1] == letter
    return first_has_letter ^ second_has_letter


def solve_b(rules):
    valid = 0
    for (letter, first, second, password) in rules:
        if is_valid_b(password, letter, first, second):
            valid += 1
    return valid


def run():
    rules = reader.read()

    print(solve_a(rules))
    print(solve_b(rules))


if __name__ == '__main__':
    run()
