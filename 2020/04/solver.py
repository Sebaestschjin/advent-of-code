import re

VALIDATORS = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': lambda v: (v[-2:] == 'cm' and (150 <= int(v[:-2]) <= 193)) or (v[-2:] == 'in' and (59 <= int(v[:-2]) <= 76)),
    'hcl': lambda v: re.match(r'^#[0-9a-f]{6}$', v),
    'ecl': lambda v: re.match(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', v),
    'pid': lambda v: re.match(r'^[0-9]{9}$', v),
}


def is_valid_a(passport):
    return 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and \
           'hcl' in passport and 'ecl' in passport and 'pid' in passport


def is_valid_b(passport):
    for n, v in VALIDATORS.items():
        try:
            if not v(passport[n]):
                return False
        except:
            return False
    return True


def solve_a(puzzle):
    valids = [p for p in puzzle if is_valid_a(p)]
    return len(valids)


def solve_b(puzzle):
    valids = [p for p in puzzle if is_valid_b(p)]
    return len(valids)


def read(filename='in'):
    with open(filename, 'r') as file:
        passports = []
        passport = {}
        for line in file.readlines():
            if not line.strip():
                passports.append(passport)
                passport = {}
            for value in [v for v in line.strip().split(' ') if v]:
                n, v = value.split(':')
                passport[n] = v

        passports.append(passport)
        return passports


def run():
    puzzle = read()

    solution_a = solve_a(puzzle)
    print(solution_a)

    solution_b = solve_b(puzzle)
    print(solution_b)


if __name__ == '__main__':
    run()
