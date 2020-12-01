def run(solver):
    with open('in') as file:
        input = [int(l) for l in list(file.readline().strip())]
        result = solver(input)
        print(result)
