def run_program(memory):
    memory = list(memory)
    pc = 0

    while pc >= 0 and pc < len(memory):
        op_code = memory[pc]
        op = OP_CODES.get(op_code)

        if not op:
            raise ValueError(f'Unknown OP-Code: {op_code}')

        pc = op(memory, pc)

    return memory


def add(memory, pc):
    left, right, target = get_values(memory, pc, 3)
    memory[target] = left + right
    return pc + 4


def multiply(memory, pc):
    left, right, target = get_values(memory, pc, 3)
    memory[target] = left * right
    return pc + 4


def halt(memory, pc):
    return -1


def get_values(memory, pc, arg_count):
    args = [memory[val] for val in memory[(pc + 1):(pc + arg_count)]]
    args.append(memory[pc + arg_count])
    return args


OP_CODES = {
    1: add,
    2: multiply,
    99: halt
}
