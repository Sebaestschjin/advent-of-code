from functools import reduce

from . import reader


def is_field_valid(field, rule):
    _, ((lower_1, upper_1), (lower_2, upper_2)) = rule
    return lower_1 <= field <= upper_1 or lower_2 <= field <= upper_2


def is_field_valid_for_any_rule(field, rules):
    return any([is_field_valid(field, (name, rule)) for name, rule in rules.items()])


def is_ticket_valid(ticket, rules):
    return all([is_field_valid_for_any_rule(field, rules) for field in ticket])


def is_rule_valid_for_index(tickets, index, rule):
    return all(is_field_valid(ticket[index], rule) for ticket in tickets)


def get_valid_rule_combinations(possible_rules, index, already_used):
    if index >= len(possible_rules):
        return already_used

    already_used_names = [name for name, _ in already_used]
    available_rules = [(name, index) for name, index in possible_rules[index] if name not in already_used_names]
    if not available_rules:
        return None

    for available in available_rules:
        next_already_used = already_used + [available]
        next_valid = get_valid_rule_combinations(possible_rules, index + 1, next_already_used)
        if next_valid:
            return next_valid

    return None


def solve_a(rules, tickets):
    invalid_ticket_fields = [field for ticket in tickets for field in ticket if
                             not is_field_valid_for_any_rule(field, rules)]
    return sum(invalid_ticket_fields)


def solve_b(rules, tickets):
    valid_tickets = [ticket for ticket in tickets if is_ticket_valid(ticket, rules)]

    possibles_rules = []
    ticket_length = len(tickets[0])
    for i in range(ticket_length):
        possible_at_index = [(name, i) for name, rule in rules.items()
                             if is_rule_valid_for_index(valid_tickets, i, (name, rule))]
        possibles_rules.append(possible_at_index)

    possibles_rules = sorted(possibles_rules, key=len)

    valid_combination = get_valid_rule_combinations(possibles_rules, 0, [])

    departure_fields = [tickets[0][index] for name, index in valid_combination if name.startswith('departure')]

    return reduce(lambda x, y: x * y, departure_fields)


def run():
    rules, tickets = reader.read()

    print(solve_a(rules, tickets))
    print(solve_b(rules, tickets))


if __name__ == '__main__':
    run()
