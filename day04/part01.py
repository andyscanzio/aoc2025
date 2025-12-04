with open("day04/input.txt", "r") as file:
    lines = file.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    grid = "".join(lines)


def index(x: int, y: int) -> int:
    return y * width + x


def reverse_index(idx: int) -> tuple[int, int]:
    y, x = divmod(idx, width)
    return x, y


def count_neighbors(idx: int) -> int:
    x, y = reverse_index(idx)
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[index(nx, ny)] == "@":
                    count += 1
    return count


print(sum(1 for i, spot in enumerate(grid) if spot == "@" and count_neighbors(i) < 4))
