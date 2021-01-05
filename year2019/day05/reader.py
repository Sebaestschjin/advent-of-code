from common.reader import read_single


def read(filename='in'):
    return read_single(__file__, filename, splitter=',', mapper=int)
