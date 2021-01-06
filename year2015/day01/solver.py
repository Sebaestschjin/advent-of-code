def solve_a(puzzle):
    open_parens = len([paren for paren in puzzle if paren == '('])
    closed_parens = len([paren for paren in puzzle if paren == ')'])

    return open_parens - closed_parens


def solve_b(puzzle):
    level = 0
    for i in range(len(puzzle)):
        paren = puzzle[i]
        if paren == '(':
            level += 1
        else:
            level -= 1
        if level < 0:
            return i + 1
