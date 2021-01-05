import argparse
import importlib
from pathlib import Path
import sys
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('year', metavar='y', type=int,
                        help='The year.')
    parser.add_argument('day', metavar='d', type=int,
                        help='The day.')
    return parser.parse_args()


def add_python_path():
    base_path = Path(__file__).parent.parent
    sys.path.append(str(base_path))


def run_solution(name, solver, input_file, additional_input):
    print(f'----- {name} ----- ')
    start_time = time.process_time()
    if additional_input:
        solution = solver(input_file, *additional_input)
    else:
        solution = solver(input_file)
    print(solution)
    print('%.2f seconds' % (time.process_time() - start_time))


def run():
    args = parse_args()
    year = args.year
    day = str(args.day).zfill(2)

    print(f'===== {year}.{day} =====')

    try:
        add_python_path()
        reader = importlib.import_module(f'year{year}.day{day}.reader')
        solver = importlib.import_module(f'year{year}.day{day}.solver')
    except ImportError:
        print(f'No python implementation could be found for this {year}.{day}. Was is solved yet?')
        exit(1)

    input_file = reader.read()

    try:
        additional_a = solver.ADDITIONAL_INPUT_A
    except AttributeError:
        additional_a = None
    run_solution('Part 1', solver.solve_a, input_file, additional_a)

    if day != 25:
        try:
            additional_b = solver.ADDITIONAL_INPUT_B
        except AttributeError:
            additional_b = None
        run_solution('Part 2', solver.solve_b, input_file, additional_b)


if __name__ == '__main__':
    run()
