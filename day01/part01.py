with open("day01/input.txt", "r") as file:
    lines = [
        (i.removesuffix("\n")[0], i.removesuffix("\n")[1:]) for i in file.readlines()
    ]

dial = 50
password = 0

for rotation in lines:
    direction, distance = rotation
    if direction == "L":
        dial -= int(distance)
    else:
        dial += int(distance)
    dial %= 100
    if dial == 0:
        password += 1

print(password)
