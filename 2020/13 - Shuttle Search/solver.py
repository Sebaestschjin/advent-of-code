from collections import defaultdict
from math import ceil, lcm

import reader


def get_min_departure(min_departure, schedule):
    times = ceil(min_departure / schedule)
    return schedule, schedule * times


def solve_a(puzzle):
    min_departure, schedules = puzzle
    min_departures = [get_min_departure(min_departure, s) for s in schedules if s]
    minimum = min(min_departures, key=lambda x: x[1])
    schedule, minimum = minimum

    return schedule * (minimum - min_departure)


def can_ignore(schedule, schedules):
    index, value = schedule
    if not value:
        return True

    has_pre = index - value >= 0 and schedules[index - value]
    has_post = index + value < len(schedules) and schedules[index + value]
    return has_pre or has_post


def solve_b(puzzle, start_at):
    _, schedules = puzzle

    sub = defaultdict(list)

    for i in range(len(schedules)):
        schedule = schedules[i]
        if not schedule:
            continue
        sub[i].append(schedule)
        index = i - schedule
        while index >= 0:
            sub[index].append(schedule)
            index -= schedule
        index = i + schedule
        while index < len(schedules):
            sub[index].append(schedule)
            index += schedule

    least_common = [(index, lcm(*values)) for index, values in sub.items()]
    max_index, max_least_common = max(least_common, key=lambda x: x[1])

    schedules = list(zip(range(len(schedules)), schedules))
    schedules = [(index, schedule) for index, schedule in schedules if schedule]

    while (start_at + max_index) % max_least_common != 0:
        start_at += 1

    possible = False
    while not possible:
        possible = True
        for index, schedule in schedules:
            can_schedule = (start_at + index) % schedule if schedule else 0
            if can_schedule != 0:
                possible = False
                start_at += max_least_common
                break

    return start_at


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle, 100000000000000))


if __name__ == '__main__':
    run()
