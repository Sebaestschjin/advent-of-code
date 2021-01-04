import year2020.day07.reader as reader


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


def run():
    rules = reader.read()

    print(solve_a(rules))
    print(solve_b(rules))


if __name__ == '__main__':
    run()
