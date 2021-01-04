from collections import defaultdict

import year2018.day02.reader as reader


def get_distance(word1, word2):
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return distance


def remove_uncommon(word1, word2):
    result = ""

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            result += word1[i]

    return result


def solve_a(boxes):
    twos = 0
    threes = 0

    for box_id in boxes:
        counter = defaultdict(int)

        for char in box_id:
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


def solve_b(box_ids):
    length = len(box_ids)

    for i in range(length):
        for j in range(i + 1, length):
            word1 = box_ids[i]
            word2 = box_ids[j]
            if get_distance(word1, word2) == 1:
                return remove_uncommon(word1, word2)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
