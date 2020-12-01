import reader


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


def solve(input, width, height):
    layers = build_layers(input, width, height)
    layer = find_layer(layers)

    return count_pixels(layer, 1) * count_pixels(layer, 2)


if __name__ == '__main__':
    reader.run(lambda input: solve(input, 6, 25))
