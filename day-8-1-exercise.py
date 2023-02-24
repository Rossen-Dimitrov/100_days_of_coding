from math import ceil


def paint_calc(h, w, c):
    cans = ceil((h * w) / c)
    return print(f"You will need of {cans} cans")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(test_h, test_w, coverage)
