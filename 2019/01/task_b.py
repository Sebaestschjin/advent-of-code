import reader


def fuel_per_mass(mass):
    fuel = int(mass / 3) - 2

    if fuel <= 0:
        return 0
    return fuel + fuel_per_mass(fuel)


def solve(input):
    return sum([fuel_per_mass(mass) for mass in input])


if __name__ == '__main__':
    reader.run(solve)
