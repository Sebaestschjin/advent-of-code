def contains_invalid_phrases(word):
    for invalid in ['ab', 'cd', 'pq', 'xy']:
        if invalid in word:
            return True
    return False


def get_vowel_count(word):
    return len([v for v in word if v in ['a', 'e', 'i', 'o', 'u']])


def contains_double_letter(word, gap_size=0):
    next_index = gap_size + 1
    for i in range(len(word) - next_index):
        if word[i] == word[i + next_index]:
            return True
    return False


def contains_double_pair(word):
    for i in range(len(word) - 2):
        pair = word[i] + word[i + 1]
        if pair in word[(i + 2):]:
            return True
    return False


def is_nice_a(word):
    return not contains_invalid_phrases(word) \
           and get_vowel_count(word) >= 3 \
           and contains_double_letter(word)


def is_nice_b(word):
    return contains_double_pair(word) \
           and contains_double_letter(word, gap_size=1)


def solve_a(words):
    return len([word for word in words if is_nice_a(word)])


def solve_b(words):
    return len([word for word in words if is_nice_b(word)])
