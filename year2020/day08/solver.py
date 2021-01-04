import year2020.day08.reader as reader


class State:
    def __init__(self):
        self.accumulator = 0
        self.next = 0
        self.visited = []
        self.loop_detected = False


def accumulate(argument, state):
    state.accumulator += argument
    state.next += 1


def jump(argument, state):
    state.next += argument


def noop(_, state):
    state.next += 1


OPERATIONS = {
    'acc': accumulate,
    'jmp': jump,
    'nop': noop,
}


def run_program(program):
    state = State()

    while state.next < len(program):
        next_operation = state.next
        if next_operation in state.visited:
            state.loop_detected = True
            break
        state.visited.append(next_operation)
        operation, argument = program[next_operation]
        OPERATIONS[operation](argument, state)

    return state


def solve_a(program):
    return run_program(program).accumulator


def solve_b(program):
    loop = run_program(program).visited

    for path in loop:
        op, arg = program[path]
        new_op = None
        if op == 'nop':
            new_op = 'jmp'
        elif op == 'jmp':
            new_op = 'nop'
        if new_op is not None:
            new_program = program.copy()
            new_program[path] = (new_op, arg)
            result = run_program(new_program)
            if not result.loop_detected:
                return result.accumulator


def run():
    program = reader.read()

    print(solve_a(program))
    print(solve_b(program))


if __name__ == '__main__':
    run()
