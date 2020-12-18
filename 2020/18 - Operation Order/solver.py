from . import reader


def evaluate(expression):
    if type(expression) == int:
        return expression

    operator, left, right = expression
    if operator == '+':
        return evaluate(left) + evaluate(right)
    elif operator == '*':
        return evaluate(left) * evaluate(right)
    else:
        raise ValueError(f'Unknown operator {operator}')


def solve_a(expressions):
    values = [evaluate(expression) for expression in expressions]
    return sum(values)


def solve_b(expressions):
    values = [evaluate(expression) for expression in expressions]
    return sum(values)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
