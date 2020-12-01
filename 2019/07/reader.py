def run(solver):
    with open('in') as file:
        input = [int(x) for x in file.readline().strip().split(',')]
    result = solver(input)
    print(result)
