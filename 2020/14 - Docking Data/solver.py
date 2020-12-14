from collections import defaultdict

from . import reader


def to_binary(value):
    return [char for char in f'{value:036b}']


def to_int(binary):
    return int(''.join(binary), 2)


def apply_mask_a(mask, value):
    binary = to_binary(value)
    for i in range(len(mask)):
        if mask[i] != 'X':
            binary[i] = mask[i]

    return to_int(binary)


def apply_mask_b(mask, value):
    binary = to_binary(value)
    for i in range(len(mask)):
        if mask[i] != '0':
            binary[i] = mask[i]

    return ''.join(binary)


def apply_floating(mask, index):
    if index >= len(mask):
        return ['']

    possible = []
    subs = apply_floating(mask, index + 1)

    my_values = ['0', '1'] if mask[index] == 'X' else [mask[index]]
    for sub in subs:
        for my_value in my_values:
            possible.append(my_value + sub)
    return possible


def get_total_memory(memory):
    memory_values = [value for _, value in memory.items() if value != 0]
    return sum(memory_values)


def solve_a(commands):
    memory = defaultdict(int)
    current_mask = None

    for command, arguments in commands:
        if command == 'mask':
            current_mask = arguments
        else:
            address, value = arguments
            value = apply_mask_a(current_mask, value)
            memory[address] = value

    return get_total_memory(memory)


def solve_b(commands):
    memory = defaultdict(int)
    current_mask = None

    for command, arguments in commands:
        if command == 'mask':
            current_mask = arguments
        else:
            address, value = arguments
            address = apply_mask_b(current_mask, address)
            addresses = [to_int(address) for address in apply_floating(address, 0)]
            for address in addresses:
                memory[address] = value

    return get_total_memory(memory)


def run():
    commands = reader.read()

    print(solve_a(commands))
    print(solve_b(commands))


if __name__ == '__main__':
    run()
