def bkb(n):
    a = bin(n)[2::]
    a = a + str(a.count('1') % 2)
    a = a + str(a.count('1') % 2)
    return int(a, 2)

for i in range(100):
    if bkb(i) > 93:
        print(i, bkb(i))