from operator import add, mul
from functools import reduce

ops = {"+": add, "*": mul}

with open("day06/input.txt", "r") as file:
    lines = file.read().splitlines()

operations = [item for item in lines[-1].split(" ") if item]

matrix = []
inner = []
for row in zip(*lines[:-1]):
    if not all(i == " " for i in row):
        inner.append(int("".join(row)))
    else:
        matrix.append(inner)
        inner = []
matrix.append(inner)
print(sum(reduce(ops[op], row) for op, row in zip(operations, matrix)))
