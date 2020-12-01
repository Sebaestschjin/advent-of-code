import itertools


def run(input):
    found = {0: True}
    frequency = 0

    for element in itertools.cycle(input):
        frequency += element
        if frequency in found:
            return frequency
        found[frequency] = True
