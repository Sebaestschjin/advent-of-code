def fuel_per_mass(mass):
    return int(mass / 3) - 2


def fuel_per_mass_including_fuel(mass):
    fuel = int(mass / 3) - 2

    if fuel <= 0:
        return 0
    return fuel + fuel_per_mass_including_fuel(fuel)


def solve_a(puzzle):
    return sum([fuel_per_mass(mass) for mass in puzzle])


def solve_b(puzzle):
    return sum([fuel_per_mass_including_fuel(mass) for mass in puzzle])
