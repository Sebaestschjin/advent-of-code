def find_containers(rules, search_bag):
    containers = []
    for bag, rule in rules.items():
        if search_bag in rule:
            containers.append(bag)
            containers.extend(find_containers(rules, bag))

    return set(containers)


def solve_a(rules):
    return len(find_containers(rules, 'shiny gold'))


def find_contents(rules, search_bag):
    if not rules[search_bag]:
        return 1

    contents = 1
    for bag, count in rules[search_bag].items():
        contents += count * find_contents(rules, bag)
    return contents


def solve_b(rules):
    return find_contents(rules, 'shiny gold') - 1


def read(filename='in'):
    with open(filename, 'r') as file:
        rules = {}
        for line in file.readlines():
            color, rule = line.strip().split(' bags ')
            contains = rule[8:].split(', ')
            color_rules = {}
            for contain in contains:
                if contain[:2] != 'no':
                    count = int(contain[:1])
                    bag = contain[2:].replace(' bags', '').replace(' bag', '').replace('.', '')
                    color_rules[bag] = count
            rules[color] = color_rules
        return rules


def run():
    puzzle = read()

    solution_a = solve_a(puzzle)
    print(solution_a)

    solution_b = solve_b(puzzle)
    print(solution_b)


if __name__ == '__main__':
    run()
