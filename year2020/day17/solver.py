from common.gameoflife import GameOfLife

ACTIVE = '#'
INACTIVE = '.'


def active_neighbor_count(neighbors):
    return len([_ for _, state in neighbors if state == ACTIVE])


RULES = {
    INACTIVE: lambda neighbors: ACTIVE if active_neighbor_count(neighbors) == 3 else INACTIVE,
    ACTIVE: lambda neighbors: ACTIVE if active_neighbor_count(neighbors) in [2, 3] else INACTIVE,
}


def solve_a(cube):
    cube = {(x, y, 0): s for (x, y), s in cube.items()}

    game = GameOfLife(cube, RULES, default_state=INACTIVE)
    for i in range(6):
        game.play_round()
    cube = game.current_cells
    return len([position for position, state in cube.items() if state == ACTIVE])


def solve_b(hypercube):
    hypercube = {(x, y, 0, 0): s for (x, y), s in hypercube.items()}

    game = GameOfLife(hypercube, RULES, default_state=INACTIVE)
    for i in range(6):
        game.play_round()
    hypercube = game.current_cells
    return len([position for position, state in hypercube.items() if state == ACTIVE])
