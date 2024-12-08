def bkb(x, y):
    if x < y:
        return 0

    if x == y:

        return 1

    else:

        return bkb(x - 2, y) + bkb(x // 2, y) + bkb(x // 3, y)


print(bkb(38, 12) * bkb(12, 3))