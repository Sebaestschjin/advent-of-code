import year2017.day13.reader as reader


class Scanner:
    def __init__(self, depth):
        self.depth = depth
        self.direction = 1
        self.position = 0

    def __repr__(self):
        res = ''
        if self.depth == 0:
            return '...'
        for i in range(self.depth):
            res += '[' + ('S' if self.position == i else ' ') + ']'
        return res

    def move(self):
        if (self.position == 0 and self.direction < 0) or (self.position + 1 == self.depth and self.direction > 0):
            self.direction *= -1
        self.position += self.direction


class Firewall:

    def __init__(self, puzzle):
        self.packet = -1
        self.second = 0
        self.scanners = []
        self.severity = 0
        for line in puzzle:
            pos, depth = line.split(': ')
            for i in range(int(pos) - len(self.scanners)):
                self.scanners += [Scanner(0)]
            self.scanners += [Scanner(int(depth))]

    def __repr__(self):
        res = '@' + str(self.packet) + ' (' + str(self.severity) + ')\n'
        for scanner, pos in zip(self.scanners, range(len(self.scanners))):
            res += '(P)' if pos == self.packet else '   '
            res += str(scanner) + '\n'
        return res

    def simulate(self):
        for i in range(len(self.scanners)):
            self.packet += 1
            if self.scanners[i].position == 0:
                self.severity += i * self.scanners[i].depth
            for scanner in self.scanners:
                scanner.move()

    def get_severity(self):
        return self.severity


def solve_a(puzzle):
    firewall = Firewall(puzzle)
    firewall.simulate()
    return firewall.get_severity()


def solve_b(puzzle):
    pass


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
