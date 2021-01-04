import pytest
from assertpy import assert_that

import year2020.day21.reader as reader
import year2020.day21.solver as solver


def test_example_a():
    foods = [(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
             (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
             (['sqjhc', 'fvjkl'], ['soy']),
             (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])]
    result = solver.solve_a(foods)
    assert_that(result).is_equal_to(5)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(2573)


def test_example_b():
    foods = [(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
             (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
             (['sqjhc', 'fvjkl'], ['soy']),
             (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])]
    result = solver.solve_b(foods)
    assert_that(result).is_equal_to('mxmxvkd,sqjhc,fvjkl')


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to('bjpkhx,nsnqf,snhph,zmfqpn,qrbnjtj,dbhfd,thn,sthnsg')
