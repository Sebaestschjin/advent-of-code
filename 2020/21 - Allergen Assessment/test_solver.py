import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        foods = [(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
                 (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
                 (['sqjhc', 'fvjkl'], ['soy']),
                 (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])]
        result = solver.solve_a(foods)
        assert_that(result).is_equal_to(5)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(2573)

    def test_example_b(self):
        foods = [(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
                 (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
                 (['sqjhc', 'fvjkl'], ['soy']),
                 (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])]
        result = solver.solve_b(foods)
        assert_that(result).is_equal_to('mxmxvkd,sqjhc,fvjkl')

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to('bjpkhx,nsnqf,snhph,zmfqpn,qrbnjtj,dbhfd,thn,sthnsg')


if __name__ == '__main__':
    unittest.main()
