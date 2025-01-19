def zxc(x):
    y = 0
    if x // 2 >= 6:
        y = y + zxc(x//2)
    if x - 6 >= 6:
        y = y + zxc(x-6)
    if x - 1 >= 6:
        y = y + zxc(x-1)
    if x == 6:
        return 1

    return y

print(zxc(19))