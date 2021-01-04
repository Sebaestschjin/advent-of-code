from collections import defaultdict

import year2020.day06.reader as reader


def get_answers_a(group):
    answers = {}
    for person in group:
        for answer in person:
            answers[answer] = 1
    return len(answers)


def solve_a(groups):
    return sum([get_answers_a(group) for group in groups])


def get_answers_b(group):
    answers = defaultdict(int)
    for person in group:
        for answer in person:
            answers[answer] += 1
    return len([x for x, c in answers.items() if c == len(group)])


def solve_b(groups):
    return sum([get_answers_b(group) for group in groups])


def run():
    groups = reader.read()

    print(solve_a(groups))
    print(solve_b(groups))


if __name__ == '__main__':
    run()
