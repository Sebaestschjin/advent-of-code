import reader


def fuel_per_mass(mass):
    return int(mass / 3) - 2


def solve(input):
    return sum([fuel_per_mass(mass) for mass in input])


if __name__ == '__main__':
    reader.run(solve)
