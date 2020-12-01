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


def build_image(layers, width, height):
    image = layers[0]

    for layer in layers[1:]:
        for row in range(height):
            for col in range(width):
                if image[row][col] == 2 and layer[row][col] != 2:
                    image[row][col] = layer[row][col]

    return image


def solve(input, width, height):
    layers = build_layers(input, width, height)
    image = build_image(layers, width, height)

    for row in image:
        for pixel in row:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    return None


if __name__ == '__main__':
    reader.run(lambda input: solve(input, 25, 6))
