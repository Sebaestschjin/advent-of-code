class CircularList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
            self.prev_node = None

        def __repr__(self):
            return repr(self.value)

    def __init__(self):
        self.head = CircularList.Node(None)
        self.tail = CircularList.Node(None)
        self.head.next_node = self.tail
        self.head.prev_node = self.tail
        self.tail.next_node = self.head
        self.tail.prev_node = self.head

    def append(self, value):
        node = CircularList.Node(value)
        self.__append(node)
        return node

    def pop(self):
        old_head = self.head.prev_node

        self.head.prev_node = old_head.prev_node
        old_head.prev_node.next_node = self.head
        return old_head

    def slice(self, start, count):
        cl = CircularList()
        start = self.get_next(start)
        for i in range(count):
            next_start = self.get_next(start)
            self.__pop_at(start)
            cl.__append(start)
            start = next_start

        return cl

    def get_next(self, node):
        next_node = node.next_node
        if next_node == self.head or next_node == self.tail:
            return self.tail.next_node
        return next_node

    def index(self, value):
        start = self.tail.next_node
        while start != self.head:
            if start.value == value:
                return start
            start = start.next_node
        return None

    def is_empty(self):
        return self.tail.next_node == self.head

    def __append(self, node):
        old_head = self.head.prev_node

        node.next_node = self.head
        node.prev_node = old_head
        old_head.next_node = node
        self.head.prev_node = node

    def __pop_at(self, node):
        old_next = node.next_node
        old_prev = node.prev_node
        node.next_node = None
        node.prev_node = None

        old_prev.next_node = old_next
        old_next.prev_node = old_prev

    # def __repr__(self):
    # values = []
    # tmp = self.tail.next_node
    # while tmp != self.head:
    #     values.append(tmp)
    #     tmp = tmp.next_node
    # return repr(values)
