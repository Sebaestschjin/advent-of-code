def measure(depths):
    increases = 0
    last = depths[0]

    for depth in depths[1:]:
        if depth > last:
            increases += 1
        last = depth

    return increases


def solve_a(depths):
    return measure(depths)


def solve_b(depths):
    windows = [depths[x:(x + 3)] for x in range(len(depths) - 2)]
    summed_windows = [sum(x) for x in windows]

    return measure(summed_windows)
