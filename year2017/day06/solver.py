def allocate_a(memory):
    seen = []
    steps = 0

    while True:
        steps = steps + 1
        cur_max = max(memory)
        cur_index = memory.index(cur_max)
        memory[cur_index] = 0
        for i in range(1, cur_max + 1):
            idx = (cur_index + i) % len(memory)
            memory[idx] = memory[idx] + 1
        current = list(memory)
        if current in seen:
            return steps
        seen.append(current)


def allocate_b(memory):
    seen = []
    tester = None
    steps = 0

    while True:
        if tester is not None:
            steps = steps + 1
        cur_max = max(memory)
        cur_index = memory.index(cur_max)
        memory[cur_index] = 0
        for i in range(1, cur_max + 1):
            idx = (cur_index + i) % len(memory)
            memory[idx] = memory[idx] + 1
        current = list(memory)
        if current in seen:
            if tester is not None:
                return steps
            tester = current
            seen.clear()
        seen.append(current)


def solve_a(puzzle):
    return allocate_a(puzzle)


def solve_b(puzzle):
    return allocate_b(puzzle)
