from itertools import count
import hashlib


def create_md5_hash(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def find_md5_hash(key, tester):
    for i in count():
        md5_hash = create_md5_hash(f'{key}{i}')
        if tester(md5_hash):
            return i


def solve_a(key):
    return find_md5_hash(key, lambda x: x.startswith('00000'))


def solve_b(key):
    return find_md5_hash(key, lambda x: x.startswith('000000'))
