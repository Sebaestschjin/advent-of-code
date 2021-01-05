from pathlib import Path


def map_to_int_list(line):
    return [int(e) for e in list(line)]


def __identity(x):
    return x


def read_single(parent, filename='in', splitter=None, mapper=__identity):
    file_path = Path(parent).parent / filename
    with file_path.open('r') as file:
        line = file.readlines()[0].strip()
        if splitter:
            return [mapper(e) for e in line.split(splitter)]
        else:
            return mapper(line)


def read_multi(parent, filename='in', splitter=None, mapper=__identity):
    file_path = Path(parent).parent / filename
    result = []
    with file_path.open('r') as file:
        lines = file.readlines()
        for line in lines:
            if splitter:
                mapped_line = [mapper(e) for e in line.strip().split(splitter)]
            else:
                mapped_line = mapper(line.strip())
            result.append(mapped_line)

    return result
