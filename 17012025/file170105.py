def zxc(x):
    y = x
    z = ''
    if x == 0:
        z = '0'
    while y > 0:
        z = str(y%3) + z
        y = y // 3
    return z


def fye(n):
    x = zxc(n)
    c = 0
    if n%3 == 0:
        x = x + x[-2::]
    else:
        for i in x:
            c = c + int(i)

        x = x + zxc(c)

    return int(x)

m = 1000

for i in range(1000):
    b = int(str(fye(i)), 3)
    if b > 220 and b%2 == 0:
        m = min(m,b)



print(m)