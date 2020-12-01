def run(solver):
    with open('in') as file:
        input = [int(line) for line in file.readlines()]
        result = solver(input)
        print(result)
