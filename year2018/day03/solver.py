import re


class Claim:

    def __init__(self, id, top, left, width, height):
        self.id = int(id)
        self.top = int(top)
        self.left = int(left)
        self.bottom = int(top) + int(height)
        self.right = int(left) + int(width)
        self.width = int(width)
        self.height = int(height)
        self.size = self.width * self.height

    def __repr__(self):
        return f'#{self.id} @({self.top},{self.left}): {self.width}x{self.height}'


PATTERN = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def parse_claim(line):
    match = re.match(PATTERN, line)
    id = match.group(1)
    left = match.group(2)
    top = match.group(3)
    width = match.group(4)
    height = match.group(5)

    return Claim(id, top, left, width, height)


def place_claims(claims):
    fabric_size = 1000
    fabric = [[0 for x in range(fabric_size)] for y in range(fabric_size)]

    for claim in claims:
        for i in range(claim.top, claim.bottom):
            for j in range(claim.left, claim.right):
                fabric[i][j] += 1

    return fabric


def find_inches(fabric):
    inches = 0

    for row in fabric:
        for x in row:
            if x > 1:
                inches += 1

    return inches


def find_non_overlap(fabric, claims):
    for claim in claims:
        points = 0
        for i in range(claim.top, claim.bottom):
            for j in range(claim.left, claim.right):
                points += fabric[i][j]
        if points == claim.size:
            return claim.id

    return None


def solve_a(puzzle):
    claims = [parse_claim(line) for line in puzzle]

    fabric = place_claims(claims)

    return find_inches(fabric)


def solve_b(puzzle):
    claims = [parse_claim(line) for line in puzzle]

    fabric = place_claims(claims)

    return find_non_overlap(fabric, claims)
