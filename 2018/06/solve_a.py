from collections import defaultdict


class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Rectangle:

    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.right = left + width
        self.bottom = top + height
        self.width = width
        self.height = height
        self.size = width * height

    @classmethod
    def by_points(cls, top, left, bottom, right):
        width = right - left
        height = bottom - top
        return cls(top, left, width, height)

    def __repr__(self):
        return f'({self.left}, {self.top}) ({self.right}, {self.bottom}) [{self.width} x {self.height}]'


def calculate_boundaries(points):
    left = min(p.x for p in points)
    right = max(p.x for p in points)
    top = min(p.y for p in points)
    bottom = max(p.y for p in points)

    return Rectangle.by_points(top, left, bottom, right)


def get_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def fill_spaces(points, bounds):
    spaces = [[[None, None] for x in range(bounds.width)] for y in range(bounds.height)]

    for x in range(bounds.left, bounds.right):
        for y in range(bounds.top, bounds.bottom):
            current = spaces[y - bounds.top][x - bounds.left]
            for i in range(len(points)):
                id = i + 1
                point = points[i]

                dist = get_distance(point, Point(x, y))

                if current[1] == dist:
                    current[0] = None

                if current[1] is None or current[1] > dist:
                    current[0] = id
                    current[1] = dist

    return spaces


def find_biggest(spaces):
    dic = defaultdict(int)

    for x in spaces:
        for y in x:
            id = y[0]
            if id is not None:
                dic[id] += 1

    width = len(spaces[0])
    height = len(spaces)

    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width or y == height:
                id = spaces[y][x][0]
                dic[id] = 0

    dic[49] = 0

    max_index = max(dic, key=dic.get)
    return (max_index, dic[max_index])


def run(input):
    points = [Point(c[0], c[1]) for c in (x.split(',') for x in input)]
    bounds = calculate_boundaries(points)
    spaces = fill_spaces(points, bounds)
    biggest, area = find_biggest(spaces)

    #print('points', points)
    print('boundaries', bounds)
   # print('spaces', spaces)

    for x in range(len(spaces[0])):
        print([p[0] for p in spaces[x]])

    print('index', biggest, points[biggest - 1])
    print('area', area)

    return area
