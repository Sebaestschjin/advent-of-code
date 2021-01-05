from common.reader import read_multi


def read(filename='in'):
    return read_multi(__file__, filename, mapper=map_line)


def map_line(line):
    return line[0], int(line[1:])
