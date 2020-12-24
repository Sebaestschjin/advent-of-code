import unittest
from assertpy import assert_that

from common.my_collections import CircularList


class CircularListTest(unittest.TestCase):
    circular_list = None

    def setUp(self) -> None:
        self.circular_list = CircularList()

    def create_elements(self, count):
        nodes = []
        for i in range(count):
            node = self.circular_list.append(i + 1)
            nodes.append(node)
        return nodes

    def test_is_empty(self):
        assert_that(self.circular_list.is_empty()).is_true()

    def test_append(self):
        node = self.circular_list.append(1)

        assert_that(self.circular_list.is_empty()).is_false()
        assert_that(node).is_instance_of(CircularList.Node)
        assert_that(node.next_node).is_equal_to(node)
        assert_that(node.prev_node).is_equal_to(node)

    def test_append_two(self):
        first = self.circular_list.append(1)
        second = self.circular_list.append(2)

        assert_that(self.circular_list.is_empty()).is_false()
        assert_that(first).is_instance_of(CircularList.Node)
        assert_that(second).is_instance_of(CircularList.Node)
        assert_that(first.next_node).is_equal_to(second)
        assert_that(first.prev_node).is_equal_to(second)
        assert_that(second.next_node).is_equal_to(first)
        assert_that(second.prev_node).is_equal_to(first)

    def test_append_three(self):
        first, second, third = self.create_elements(3)

        assert_that(self.circular_list.is_empty()).is_false()
        assert_that(first).is_instance_of(CircularList.Node)
        assert_that(second).is_instance_of(CircularList.Node)
        assert_that(third).is_instance_of(CircularList.Node)
        assert_that(first.next_node).is_equal_to(second)
        assert_that(first.prev_node).is_equal_to(third)
        assert_that(second.next_node).is_equal_to(third)
        assert_that(second.prev_node).is_equal_to(first)
        assert_that(third.next_node).is_equal_to(first)
        assert_that(third.prev_node).is_equal_to(second)

    def test_pop(self):
        self.circular_list.append(1)

        self.circular_list.pop()

        assert_that(self.circular_list.is_empty).is_true()

    def test_pop_two(self):
        self.circular_list.append(1)
        self.circular_list.append(2)

        self.circular_list.pop()

        assert_that(self.circular_list.is_empty()).is_false()
