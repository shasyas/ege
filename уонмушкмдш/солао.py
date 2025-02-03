def zxc(a):
    b = str(a)
    c = [int(b[0]) + int(b[1]), int(b[1]) + int(b[2])]
    return int(str(min(c)) + str(max(c)))

for i in range(100, 1000):
    if zxc(i) == 1216:
        print(i)