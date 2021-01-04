import year2019.day08.reader as reader


def build_layers(input, width, height):
    image_size = width * height
    layer_count = len(input) // (width * height)
    layers = []

    for layer in range(layer_count):
        start_image = layer * image_size
        layer = []
        for y in range(height):
            start_row = start_image + y * width
            row = input[start_row:(start_row + width)]
            layer.append(row)

        layers.append(layer)

    return layers


def count_pixels(layer, value):
    count = 0
    for row in layer:
        count += len([p for p in row if p == value])
    return count


def find_layer(layers):
    cur_layer = 0
    min_zero = -1

    for index in range(len(layers)):
        layer = layers[index]
        zeros = count_pixels(layer, 0)
        if min_zero == -1 or min_zero > zeros:
            min_zero = zeros
            cur_layer = index

    return layers[cur_layer]


def build_image(layers, width, height):
    image = layers[0]

    for layer in layers[1:]:
        for row in range(height):
            for col in range(width):
                if image[row][col] == 2 and layer[row][col] != 2:
                    image[row][col] = layer[row][col]

    return image


def solve_a(puzzle, dimension):
    width, height = dimension
    layers = build_layers(puzzle, width, height)
    layer = find_layer(layers)

    return count_pixels(layer, 1) * count_pixels(layer, 2)


def solve_b(puzzle, dimension):
    width, height = dimension
    layers = build_layers(puzzle, width, height)
    image = build_image(layers, width, height)

    for row in image:
        for pixel in row:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    return None


def run():
    puzzle = reader.read()

    print(solve_a(puzzle, (6, 25)))
    print(solve_b(puzzle, (25, 6)))


if __name__ == '__main__':
    run()
