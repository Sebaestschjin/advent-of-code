from collections import defaultdict

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


def read(filename='in'):
    with open(filename, 'r') as file:
        groups = []
        group = []

        for line in file.readlines():
            if not line.strip():
                groups.append(group)
                group = []
            else:
                group.append(line.strip())

        groups.append(group)
        return groups


def run():
    puzzle = read()

    solution_a = solve_a(puzzle)
    print(solution_a)

    solution_b = solve_b(puzzle)
    print(solution_b)


if __name__ == '__main__':
    run()
