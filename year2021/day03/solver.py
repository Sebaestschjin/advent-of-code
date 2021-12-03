def binary_to_decimal(binary):
    return int(''.join([str(b) for b in binary]), 2)


def get_most_common_bit(diagnostics, position):
    bits = sum([d[position] for d in diagnostics])
    return 1 if bits >= (len(diagnostics) / 2) else 0


def get_least_common_bit(diagnostics, position):
    common = get_most_common_bit(diagnostics, position)
    return 0 if common else 1


def get_gamma_rate(diagnostics):
    bit_size = len(diagnostics[0])
    return binary_to_decimal([get_most_common_bit(diagnostics, i) for i in range(bit_size)])


def get_epsilon_rate(diagnostics):
    bit_size = len(diagnostics[0])
    return binary_to_decimal([get_least_common_bit(diagnostics, i) for i in range(bit_size)])


def do_get_rate(diagnostics, position, bit_filter):
    if len(diagnostics) == 1:
        return binary_to_decimal(diagnostics[0])

    bit = bit_filter(diagnostics, position)
    filtered = [d for d in diagnostics if d[position] == bit]
    return do_get_rate(filtered, position + 1, bit_filter)


def get_oxygen_rating(diagnostics):
    return do_get_rate(diagnostics, 0, get_most_common_bit)


def get_co2_rubber_rating(diagnostics):
    return do_get_rate(diagnostics, 0, get_least_common_bit)


def solve_a(diagnostics):
    gamma_rate = get_gamma_rate(diagnostics)
    epsilon_rate = get_epsilon_rate(diagnostics)

    return gamma_rate * epsilon_rate


def solve_b(diagnostics):
    oxygen_rating = get_oxygen_rating(diagnostics)
    co_rubber_rating = get_co2_rubber_rating(diagnostics)

    return oxygen_rating * co_rubber_rating
