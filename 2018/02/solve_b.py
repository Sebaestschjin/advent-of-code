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


def run(input):
    length = len(input)

    for i in range(length):
        for j in range(i + 1, length):
            word1 = input[i]
            word2 = input[j]
            if get_distance(word1, word2) == 1:
                return remove_uncommon(word1, word2)

    return None
