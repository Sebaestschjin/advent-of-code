from collections import defaultdict
from functools import reduce

import year2020.day21.reader as reader


def get_foods_per_allergen(foods):
    food_per_allergen = defaultdict(list)
    for ingredients, allergens in foods:
        for allergen in allergens:
            food_per_allergen[allergen].append(ingredients)

    return food_per_allergen


def union(left, right):
    return [l for l in left if l in right]


def get_possible_allergen_per_ingredient(food_per_allergen):
    allergen_per_ingredients = {}
    for allergen, foods in food_per_allergen.items():
        ingredient = reduce(union, foods)
        allergen_per_ingredients[allergen] = ingredient

    return allergen_per_ingredients


def allergens_detected(possible_allergens):
    return all([len(possible) == 1 for possible in possible_allergens.values()])


def detect_allergens(food_per_allergen):
    possible_allergens = get_possible_allergen_per_ingredient(food_per_allergen)
    while not allergens_detected(possible_allergens):
        for allergen, x_possible in possible_allergens.items():
            if len(x_possible) == 1:
                detected = x_possible[0]
                for possible in [p for p in possible_allergens.values() if p != x_possible]:
                    if detected in possible:
                        possible.remove(detected)
    return possible_allergens


def get_allergic_ingredients(foods):
    food_per_allergen = get_foods_per_allergen(foods)
    allergen_per_ingredient = detect_allergens(food_per_allergen)

    allergic_ingredients = {}
    for allergen, ingredient in allergen_per_ingredient.items():
        allergic_ingredients[ingredient[0]] = allergen
    return allergic_ingredients


def solve_a(foods):
    allergic_ingredients = get_allergic_ingredients(foods)
    non_allergic = [ingredient for ingredients, _ in foods for ingredient in ingredients
                    if ingredient not in allergic_ingredients]
    return len(non_allergic)


def solve_b(foods):
    allergic_ingredients = get_allergic_ingredients(foods)
    return ','.join(dict(sorted(allergic_ingredients.items(), key=lambda i: i[1])).keys())


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
