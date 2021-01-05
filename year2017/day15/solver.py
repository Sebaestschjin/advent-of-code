FACTORS = {'A': 16807, 'B': 48271}


class Generator:
    DIVIDER = 2147483647

    def __init__(self, generator, multiplier=None):
        self.name, self.current = generator
        self.factor = FACTORS[self.name]
        self.multiplier = multiplier

    def next(self):
        cur = (self.current * self.factor) % self.DIVIDER
        self.current = cur
        if self.multiplier and self.current % self.multiplier != 0:
            self.next()


class Judge:
    def __init__(self):
        self.valid = 0

    def judge(self, generators):
        to_test = None
        for g in generators:
            byt = g.current.to_bytes(4, byteorder='big')
            if to_test is None:
                to_test = byt[2:]
            if byt[2:] != to_test:
                return False
        self.valid += 1
        return True


def solve_a(puzzle):
    sample_size = 40000000
    judge = Judge()
    generators = [Generator(generator) for generator in puzzle]
    for i in range(sample_size):
        for gen in generators:
            gen.next()
        judge.judge(generators)
    return judge.valid


def solve_b(puzzle):
    sample_size = 5000000
    judge = Judge()
    multipliers = {'A': 4, 'B': 8}
    generators = [Generator(generator, multiplier=multipliers[generator[0]]) for generator in puzzle]
    for i in range(sample_size):
        for gen in generators:
            gen.next()
        judge.judge(generators)
    return judge.valid
