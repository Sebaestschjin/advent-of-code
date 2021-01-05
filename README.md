![Run Python Tests](https://github.com/Sebaestschjin/advent-of-code/workflows/Run%20Python%20Tests/badge.svg)

My solutions to advent of code. Written in Python. Some newer solutions require Python 3.9+. Most other stuff should
work with 3.6+.

# Progress

Total: 108/300

# Goals

* use test-driven development
* write readable and clone code
* try to reuse code
* complete all challenges

# Usage

## Create files for a new day

Run the script `scripts/create.py` with the year and day as parameters. This will create a new directory for this day
and copy all files from the `template` directory. Template files (ending with `.mustache`) wil be rendered and then
saved. The input file will be automatically loaded and written to the file `in`. This requires that the AOC
Session-Token is available on the system (more information on [https://pypi.org/project/advent-of-code-data/]).

## Run the solution for a given day

Run the script `scripts/run.py` with the year and day as parameters.
