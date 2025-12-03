with open("day03/input.txt", "r") as file:
    lines = file.read().splitlines()


def max_jolt(bank: str) -> int:
    i, j = 0, 1
    for x, k in enumerate(bank):
        if int(k) > int(bank[i]) and x < len(bank) - 1:
            i = x
            j = x + 1
        elif int(k) > int(bank[j]) and x > j:
            j = x
    return int(bank[i] + bank[j])


print(sum(max_jolt(line) for line in lines))
