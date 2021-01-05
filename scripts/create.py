#!/bin/env python

from aocd.models import Puzzle
import argparse
import chevron
import os
from pathlib import Path
from shutil import copy


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('year', metavar='y', type=int,
                        help='The year.')
    parser.add_argument('day', metavar='d', type=int,
                        help='The day.')
    return parser.parse_args()


def run():
    args = parse_args()
    year = args.year
    day = args.day

    base_path = Path(__file__).parent.parent
    solution_path = base_path / f'year{year}' / f'day{str(day).zfill(2)}'
    os.makedirs(str(solution_path), exist_ok=True)

    for file in (base_path / 'template').iterdir():
        if file.name == '__pycache__':
            continue

        if file.name == 'in':
            in_file = copy(file, solution_path)
            in_file = Path(in_file)
            puzzle = Puzzle(year=year, day=day)
            in_file.write_text(puzzle.input_data)
        elif file.suffix == '.mustache':
            with open(file, 'r') as template:
                rendered_content = chevron.render(template, {'year': year, 'day': day})

            copied_file = Path(solution_path) / file.name.replace('.mustache', '.py')
            copied_file.write_text(rendered_content)
        else:
            copy(file, solution_path)


if __name__ == '__main__':
    run()
