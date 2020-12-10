from collections import defaultdict

import reader

def get_all_adapters(adapters):
    adapters.append(0)                  # the outlet
    adapters.append(max(adapters) + 3)  # the device
    return sorted(adapters)


def solve_a(adapters):
    adapters = get_all_adapters(adapters)

    differences = defaultdict(int)
    for i in range(len(adapters) - 1):
        difference = adapters[i+1] - adapters[i]
        differences[difference] += 1

    return differences[1] * differences[3]


def get_possible_connections(current, adapters):
    return [adapter for adapter in adapters if 1 <= adapter - current <= 3]


def get_connection_count(current, adapters, already_calculated):
    possible_connections = get_possible_connections(current, adapters)
    if not possible_connections:
        return 1

    total_connection_count = 0
    for possible in possible_connections:
        if possible in already_calculated:
            total_connection_count += already_calculated[possible]
        else:
            connection_count = get_connection_count(possible, adapters, already_calculated)
            already_calculated[possible] = connection_count
            total_connection_count += connection_count
    return total_connection_count


def solve_b(adapters):
    adapters = get_all_adapters(adapters)

    return get_connection_count(0, adapters, {})


def run():
    adapters = reader.read()

    print(solve_a(adapters))
    print(solve_b(adapters))


if __name__ == '__main__':
    run()
