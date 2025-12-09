from operator import add, mul
from functools import reduce

ops = {"+": add, "*": mul}

with open("day06/input.txt", "r") as file:
    lines = file.read().splitlines()

complete_matrix = [[item for item in line.split(" ") if item] for line in lines]
transposed_matrix, operations = [
    list(map(int, row)) for row in complete_matrix[:-1]
], complete_matrix[-1]

matrix = list(zip(*transposed_matrix))

print(sum(reduce(ops[op], row) for op, row in zip(operations, matrix)))
