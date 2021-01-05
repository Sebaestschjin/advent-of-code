from common.reader import read_single, map_to_int_list


def read(filename='in'):
    return read_single(__file__, filename, mapper=map_to_int_list)
