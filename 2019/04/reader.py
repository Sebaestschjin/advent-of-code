def run(solver):
    with open('in') as file:
        input = file.readline().strip().split('-')
        result = solver(input)
        print(result)
