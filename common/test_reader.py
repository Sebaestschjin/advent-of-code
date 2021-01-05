from assertpy import assert_that

import common.reader as reader


def test_read_single(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345\n')

    result = reader.read_single(file)

    assert_that(result).is_equal_to('12345')


def test_read_single_with_splitter(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345 67890\n')

    result = reader.read_single(file, splitter=' ')

    assert_that(result).is_equal_to(['12345', '67890'])


def test_read_single_with_mapper(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345\n')

    result = reader.read_single(file, mapper=int)

    assert_that(result).is_equal_to(12345)


def test_read_single_with_splitter_and_mapper(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345 67890\n')

    result = reader.read_single(file, splitter=' ', mapper=int)

    assert_that(result).is_equal_to([12345, 67890])


def test_read_multi(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345\n6789\n')

    result = reader.read_multi(file)

    assert_that(result).is_equal_to(['12345', '6789'])


def test_read_multi_with_splitter(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345,abc\n6789,def\n')

    result = reader.read_multi(file, splitter=',')

    assert_that(result).is_equal_to([['12345', 'abc'], ['6789', 'def']])


def test_read_multi_with_splitter_and_mapper(tmp_path):
    file = tmp_path / "in"
    file.write_text('12345,-1,-2\n6789,-3,-4\n')

    result = reader.read_multi(file, splitter=',', mapper=int)

    assert_that(result).is_equal_to([[12345, -1, -2], [6789, -3, -4]])
