def run(solver):
    with open('in') as file:
        input = [line.strip().split(',') for line in file.readlines()]
        result = solver(input)
        print(result)
