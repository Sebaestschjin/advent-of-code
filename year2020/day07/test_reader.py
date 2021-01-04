from assertpy import assert_that

import year2020.day07.reader as reader


def test_example():
    lines = ['light red bags contain 1 bright white bag, 2 muted yellow bags.\n',
             'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n',
             'bright white bags contain 1 shiny gold bag.\n',
             'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n',
             'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n',
             'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n',
             'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n',
             'faded blue bags contain no other bags.\n',
             'dotted black bags contain no other bags.\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to({'light red': {'bright white': 1, 'muted yellow': 2},
                                     'dark orange': {'bright white': 3, 'muted yellow': 4},
                                     'bright white': {'shiny gold': 1},
                                     'muted yellow': {'shiny gold': 2, 'faded blue': 9},
                                     'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
                                     'dark olive': {'faded blue': 3, 'dotted black': 4},
                                     'vibrant plum': {'faded blue': 5, 'dotted black': 6},
                                     'faded blue': {},
                                     'dotted black': {},
                                     })
