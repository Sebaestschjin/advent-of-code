import sebaestschjin.files as files

import solve_a
import solve_b

use_b = True


if __name__ == '__main__':
    input = files.read_first("in")

    if use_b:
        result = solve_b.run(input)
    else:
        result = solve_a.run(input)
    print(result)
