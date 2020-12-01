
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


def run(input):
    chars = [x for x in input]

    return collapse(chars)
