def collapse(polymer):
    chars = polymer.copy()

    index = 0
    while index + 1 < len(chars):
        this = chars[index]
        next = chars[index + 1]

        if this.lower() == next.lower() and this != next:
            del chars[index]
            del chars[index]
            index = max(0, index - 1)
        else:
            index += 1

    return len(chars)


def remove(polymer, component):
    lower = str(chr(component + 97))
    upper = lower.upper()

    return [x for x in polymer if x != lower and x != upper]


def solve_a(puzzle):
    return collapse(list(puzzle))


def solve_b(puzzle):
    cur_min = None
    chars = list(puzzle)
    for char in range(26):
        size = collapse(remove(chars, char))
        if not cur_min or cur_min > size:
            cur_min = size

    return cur_min
