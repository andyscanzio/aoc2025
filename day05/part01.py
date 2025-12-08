from typing import Callable

with open("day05/input.txt", "r") as file:
    lines = file.read().split("\n\n")
    parse_range: Callable[[str], tuple[int, int]] = lambda t: (
        int(t.split("-")[0]),
        int(t.split("-")[1]),
    )
    ranges, ingredients = list(map(parse_range, lines[0].splitlines())), list(
        map(int, lines[1].splitlines())
    )


total = 0
for ingredient in ingredients:
    for a, b in ranges:
        if a <= ingredient <= b:
            total += 1
            break
print(total)
