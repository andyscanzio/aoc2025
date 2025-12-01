with open("day01/input.txt", "r") as file:
    lines = [
        (i.removesuffix("\n")[0], i.removesuffix("\n")[1:]) for i in file.readlines()
    ]
previous_dial = 50
dial = 50
password = 0

for rotation in lines:
    direction, distance = rotation
    rotations, remainder = divmod(int(distance), 100)
    if direction == "L":
        dial = previous_dial - remainder
    else:
        dial = previous_dial + remainder
    password += rotations
    if (
        (previous_dial > 0 and dial < 0)
        or (previous_dial < 100 and dial > 100)
        or dial % 100 == 0
    ):
        password += +1
    previous_dial = dial % 100


print(password)
