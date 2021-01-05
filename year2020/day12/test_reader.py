from assertpy import assert_that

import year2020.day12.reader as reader


def test_example(tmp_path):
    in_file = tmp_path / 'in'
    in_file.write_text('F10\nN3\nF7\nR90\nF11\n')

    result = reader.read(in_file)

    assert_that(result).is_equal_to([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
