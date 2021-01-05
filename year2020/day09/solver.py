ADDITIONAL_INPUT_A = [25]
ADDITIONAL_INPUT_B = [25]


def is_valid(number, part):
    for i in range(len(part)):
        for j in range(len(part)):
            if i != j and part[i] + part[j] == number:
                return True
    return False


def solve_a(data, preamble_size):
    for i in range(preamble_size, len(data)):
        number = data[i]
        start = i - preamble_size
        end = i
        if not is_valid(number, data[start:end]):
            return number


def solve_b(data, preamble_size):
    invalid_number = solve_a(data, preamble_size)

    for i in range(len(data)):
        total = data[i]
        for j in range(i + 1, len(data)):
            total += data[j]
            if total == invalid_number:
                min_number = min(data[i:j])
                max_number = max(data[i:j])
                return min_number + max_number
            if total > invalid_number:
                break
