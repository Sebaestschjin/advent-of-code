import re
from typing import List, Union

import year2020.day19.reader as reader

Rule = type(Union[int, str, List[int], List[List[int]]])


def use_special_handling(rules, rule):
    return (rule == 8 and rules[8] == [[42], [42, 8]]) \
           or (rule == 11 and rules[11] == [[42, 31], [42, 11, 31]])


def create_validator_with_special_handling(rules, rule):
    if rule == 8:
        return create_validator_for(rules, 42) + '+'
    if rule == 11:
        left = create_validator_for(rules, 42)
        right = create_validator_for(rules, 31)
        combinations = [left * times + right * times for times in range(1, 5)]
        return '(' + '|'.join(combinations) + ')'
    return None


def create_validator_for(rules: dict[int, Rule], rule: Rule):
    if use_special_handling(rules, rule):
        return create_validator_with_special_handling(rules, rule)
    elif type(rule) == int:
        return create_validator_for(rules, rules[rule])
    elif type(rule) == str:
        return rule
    elif type(rule) == list and type(rule[0]) == list:
        return '(' + '|'.join([create_validator_for(rules, part) for part in rule]) + ')'
    else:
        return ''.join([create_validator_for(rules, part) for part in rule])


def create_validator(rules: dict[int, Rule]):
    return '^' + create_validator_for(rules, 0) + '$'


def is_valid(validator, word):
    return re.match(validator, word)


def solve_a(rules, words):
    validator = create_validator(rules)
    return len([word for word in words if is_valid(validator, word)])


def solve_b(rules, words):
    validator = create_validator(rules)
    return len([word for word in words if is_valid(validator, word)])


def run():
    rules, words = reader.read()

    print(solve_a(rules, words))

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    print(solve_b(rules, words))


if __name__ == '__main__':
    run()
