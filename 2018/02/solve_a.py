from collections import defaultdict


def run(input):

    twos = 0
    threes = 0

    for id in input:
        counter = defaultdict(int)

        for char in id:
            counter[char] += 1

        have_three = False
        have_two = False
        for c, v in counter.items():
            if v == 3 and not have_three:
                threes += 1
                have_three = True
            if v == 2 and not have_two:
                twos += 1
                have_two = True

    return twos * threes
