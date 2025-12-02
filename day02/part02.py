from re import match, compile

with open("day02/input.txt", "r") as file:
    ranges = [tuple(map(int, i.split("-"))) for i in file.read().split(",")]

PATTERN = compile(r"^(\d+)\1+$")

total = 0
for start, end in ranges:
    for i in range(start, end + 1):
        if match(PATTERN, str(i)):
            total += i
print(total)
