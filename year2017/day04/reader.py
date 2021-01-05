from common.reader import read_multi


def read(filename='in'):
    return read_multi(__file__, filename, splitter=' ')
