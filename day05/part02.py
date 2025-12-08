from typing import Callable

with open("day05/input.txt", "r") as file:
    lines = file.read().split("\n\n")
    parse_range: Callable[[str], tuple[int, int]] = lambda t: (
        int(t.split("-")[0]),
        int(t.split("-")[1]),
    )
    ranges = list(map(parse_range, lines[0].splitlines()))

merged: list[tuple[int, int]] = []

ranges = sorted(ranges, key=lambda r: r[0])

merged = []
current_start, current_end = ranges[0]

for start, end in ranges[1:]:
    if start <= current_end:
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))


print(sum(b - a + 1 for a, b in merged))
