from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    foods = []
    for line in lines:
        line = line.strip().replace(')', '')
        ingredients, allergens = line.strip().split(' (contains ')
        foods.append((ingredients.split(' '), allergens.split(', ')))
    return foods
