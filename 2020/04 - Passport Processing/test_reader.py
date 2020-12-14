import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
                 'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
                 '\n',
                 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
                 'hcl:#cfa07d byr:1929\n',
                 '\n',
                 'hcl:#ae17e1 iyr:2013\n',
                 'eyr:2024\n',
                 'ecl:brn pid:760753108 byr:1931\n',
                 'hgt:179cm\n',
                 '\n',
                 'hcl:#cfa07d eyr:2025 pid:166559648\n',
                 'iyr:2011\n',
                 'ecl:brn\n',
                 'hgt:59in\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([
            {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
             'cid': '147', 'hgt': '183cm'},
            {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d',
             'byr': '1929'},
            {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931',
             'hgt': '179cm'},
            {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}])


if __name__ == '__main__':
    unittest.main()
