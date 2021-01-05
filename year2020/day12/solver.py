class Navigation:
    DIRECTIONS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    ROTATIONS = {
        'L': -1,
        'R': 1,
    }

    def __init__(self, instructions, waypoint=None):
        self.x, self.y = (0, 0)
        if waypoint:
            self.waypoint_x, self.waypoint_y = waypoint
            self.use_waypoint = True
        else:
            self.use_waypoint = False
        self.direction = 'E'
        self.rotation = 90
        self.instructions = instructions

    def run(self):
        for action, value in self.instructions:
            # print('----', action, value, '----')
            # print('@', self.x, self.y)
            # if self.use_waypoint:
            #     print('t', self.waypoint_x, self.waypoint_y)

            if action in ['N', 'E', 'S', 'W']:
                self.move(action, value)
            elif action == 'F':
                self.move_forward(value)
            elif action in ['R', 'L']:
                self.turn(action, value)
        return self.x, self.y

    def move(self, direction, value):
        add_x, add_y = self.DIRECTIONS[direction]
        if self.use_waypoint:
            self.waypoint_x += add_x * value
            self.waypoint_y += add_y * value
        else:
            self.x += add_x * value
            self.y += add_y * value

    def move_forward(self, value):
        if self.use_waypoint:
            self.x += self.waypoint_x * value
            self.y += self.waypoint_y * value
        else:
            self.move(self.direction, value)

    def turn(self, direction, value):
        rotation = self.ROTATIONS[direction]
        if self.use_waypoint:
            current_x, current_y = self.waypoint_x, self.waypoint_y
            normalized_rotation = (int(value / 90) * rotation) % 4
            if normalized_rotation == 2:
                self.waypoint_x *= -1
                self.waypoint_y *= -1
            elif normalized_rotation == 1:
                self.waypoint_x = current_y
                self.waypoint_y = -current_x
            elif normalized_rotation == 3:
                self.waypoint_x = -current_y
                self.waypoint_y = current_x
        else:
            self.rotation += rotation * value
            self.rotation = self.rotation % 360
            if self.rotation == 0:
                self.direction = 'N'
            elif self.rotation == 90:
                self.direction = 'E'
            elif self.rotation == 180:
                self.direction = 'S'
            elif self.rotation == 270:
                self.direction = 'W'
            else:
                raise ValueError(self.rotation)


def get_distance(from_position, to_position):
    from_x, from_y = from_position
    to_x, to_y = to_position
    return abs(from_x - to_x), abs(from_y - to_y)


def solve_a(instructions):
    navigation = Navigation(instructions)
    final_position = navigation.run()
    dist_x, dist_y = get_distance((0, 0), final_position)
    return dist_x + dist_y


def solve_b(instructions):
    navigation = Navigation(instructions, waypoint=(10, 1))
    final_position = navigation.run()
    dist_x, dist_y = get_distance((0, 0), final_position)
    return dist_x + dist_y
