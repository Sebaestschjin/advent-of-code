import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_find_loop_1(self):
        key = 5764801
        subject, divisor = 7, 20201227
        loop_size = solver.find_loop_size(key, subject, divisor)
        assert_that(loop_size).is_equal_to(8)

    def test_find_loop_2(self):
        key = 17807724
        subject, divisor = 7, 20201227
        loop_size = solver.find_loop_size(key, subject, divisor)
        assert_that(loop_size).is_equal_to(11)

    def test_calculate_encryption_key_1(self):
        subject = 17807724
        loop_size, divisor = 8, 20201227
        encryption_key = solver.calculate_encryption_key(subject, loop_size, divisor)
        assert_that(encryption_key).is_equal_to(14897079)

    def test_calculate_encryption_key_2(self):
        subject = 5764801
        loop_size, divisor = 11, 20201227
        encryption_key = solver.calculate_encryption_key(subject, loop_size, divisor)
        assert_that(encryption_key).is_equal_to(14897079)

    def test_example_a(self):
        public_keys = [5764801, 17807724]
        result = solver.solve_a(public_keys)
        assert_that(result).is_equal_to(14897079)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(296776)


if __name__ == '__main__':
    unittest.main()
