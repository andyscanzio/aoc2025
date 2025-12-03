with open("day03/input.txt", "r") as file:
    lines = [list(map(int, list(line))) for line in file.read().splitlines()]


def max_jolt(bank: list[int]) -> int:
    stack: list[int] = []
    for i, k in enumerate(bank):
        if len(bank) - i <= 12 - len(stack):
            stack.append(k)
        else:
            for j, x in enumerate(stack):
                if k > x and len(bank) - i >= 12 - j:
                    del stack[j:]
                    stack.append(k)
                    break
            else:
                if len(stack) < 12:
                    stack.append(k)

    return int("".join(map(str, stack)))


print(sum(max_jolt(line) for line in lines))
