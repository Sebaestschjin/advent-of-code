from assertpy import assert_that

import year2017.day07.reader as reader


def test_example():
    lines = ['ktlj (57)\n',
             'fwft (72) -> ktlj, cntj, xhth\n',
             'qoyq (66)\n',
             'padx (45) -> pbga, havc, qoyq\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([
        ('ktlj', 57, []),
        ('fwft', 72, ['ktlj', 'cntj', 'xhth']),
        ('qoyq', 66, []),
        ('padx', 45, ['pbga', 'havc', 'qoyq'])])
