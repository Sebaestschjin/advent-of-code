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
