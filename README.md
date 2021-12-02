![Run Python Tests](https://github.com/Sebaestschjin/advent-of-code/workflows/Run%20Python%20Tests/badge.svg)

My solutions to advent of code. Written in Python. Some newer solutions require Python 3.9+. Most other stuff should
work with 3.6+.

# Progress

| Year | Stars |
| --- | --- | 
| 2021 | [![2021](https://img.shields.io/badge/stars%20⭐-2-yellow)](https://adventofcode.com/2021/stats) |
| 2020 | [![2020](https://img.shields.io/badge/stars%20⭐-50-yellow)](https://adventofcode.com/2020/stats) |
| 2019 | [![2019](https://img.shields.io/badge/stars%20⭐-16-yellow)](https://adventofcode.com/2019/stats) |
| 2018 | [![2018](https://img.shields.io/badge/stars%20⭐-12-yellow)](https://adventofcode.com/2018/stats) |
| 2017 | [![2017](https://img.shields.io/badge/stars%20⭐-2-yellow)](https://adventofcode.com/2017/stats) |
| 2016 | [![2016](https://img.shields.io/badge/stars%20⭐-0-yellow)](https://adventofcode.com/2016/stats) |
| 2015 | [![2015](https://img.shields.io/badge/stars%20⭐-10-yellow)](https://adventofcode.com/2015/stats) |

# Goals

* use test-driven development
* write readable and clean code
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
