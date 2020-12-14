import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(25)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(998)

    def test_example_turn_right(self):
        self.run_turn_test(('R', 90), (10, 5), (5, -10))
        self.run_turn_test(('R', 180), (10, 5), (-10, -5))
        self.run_turn_test(('R', 270), (10, 5), (-5, 10))
        self.run_turn_test(('R', 360), (10, 5), (10, 5))

    def test_example_turn_left(self):
        self.run_turn_test(('L', 90), (10, 5), (-5, 10))
        self.run_turn_test(('L', 180), (10, 5), (-10, -5))
        self.run_turn_test(('L', 270), (10, 5), (5, -10))
        self.run_turn_test(('L', 360), (10, 5), (10, 5))

    def test_example_turn_move(self):
        nav = solver.Navigation([], waypoint=(10, 10))
        nav.x = 1
        nav.y = 1
        nav.turn('R', 270)
        nav.move_forward(1)
        assert_that(nav.waypoint_x).is_equal_to(-10)
        assert_that(nav.waypoint_y).is_equal_to(10)
        assert_that(nav.x).is_equal_to(-9)
        assert_that(nav.y).is_equal_to(11)

    def run_turn_test(self, turn, waypoint, expected, start=(0, 0)):
        nav = solver.Navigation([], waypoint=waypoint)
        x, y = start
        expected_x, expected_y = expected
        action, value = turn
        nav.x = x
        nav.y = y
        nav.turn(action, value)
        assert_that(nav.waypoint_x).is_equal_to(expected_x)
        assert_that(nav.waypoint_y).is_equal_to(expected_y)

    def test_example_b(self):
        puzzle = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(286)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(71586)


if __name__ == '__main__':
    unittest.main()
