def solve_a(directions):
    position = 0
    current_depth = 0

    for movement, depth in directions:
        position += movement
        current_depth += depth

    return position * current_depth


def solve_b(directions):
    current_aim = 0
    position = 0
    current_depth = 0

    for movement, aim in directions:
        current_aim += aim
        position += movement
        current_depth += (movement * current_aim)

    return position * current_depth
