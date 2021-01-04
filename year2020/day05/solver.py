import year2020.day05.reader as reader


def binary_search(down, up, splitter):
    half = (up + down + 1) / 2
    if splitter[0] == 'F' or splitter[0] == 'L':
        return binary_search(down, half - 1, splitter[1:]) if len(splitter) > 1 else int(down)
    else:
        return binary_search(half, up, splitter[1:]) if len(splitter) > 1 else int(up)


def get_seat_position(boarding_pass):
    row = binary_search(0, 127, boarding_pass[:7])
    col = binary_search(0, 7, boarding_pass[7:])
    return row, col


def get_seat_id(position):
    row, col = position
    return row * 8 + col


def solve_a(boarding_passes):
    return max([get_seat_id(pos) for pos in [get_seat_position(boarding) for boarding in boarding_passes]])


def solve_b(boarding_passes):
    seats = [get_seat_position(boarding) for boarding in boarding_passes]
    seat_ids = [get_seat_id(position) for position in seats]
    all_seats = []
    for row in range(128):
        for col in range(8):
            all_seats.append((row, col))
    missing_seats = [p for p in all_seats if p not in seats]

    for missing_seat in missing_seats:
        seat_id = get_seat_id(missing_seat)
        if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
            return seat_id


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
