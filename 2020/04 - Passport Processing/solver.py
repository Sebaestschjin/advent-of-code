import re

from . import reader

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
        except KeyError:
            return False
    return True


def solve_a(passports):
    valid_passports = [p for p in passports if is_valid_a(p)]
    return len(valid_passports)


def solve_b(passports):
    valid_passports = [p for p in passports if is_valid_b(p)]
    return len(valid_passports)


def run():
    passports = reader.read()

    print(solve_a(passports))
    print(solve_b(passports))


if __name__ == '__main__':
    run()
