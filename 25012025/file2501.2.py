files = ['27a2.txt', '27b2.txt']
c = [2, 6]
h = 10000

def zxc(p, t):
    x, y = p
    if t == 0:
        return y < 0
    if x > 0:
        return y > 0
    elif y > -25:
        return 2
    return 3


def fye(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


for t in range(2):
    fo = open(str(files[t]))
    fo.readline()
    cs = [[], [], [], [], [], []]
    n = c[t]

    for line in fo:
        p = [float(d) for d in line.replace(',', '.').split()]
        cs[zxc(p, t)].append(p)

    ms = []

    for i in range(n):
        dm = 10**1000

        for p in cs[i]:
            d = sum(fye(p, j) for j in cs[i])
            if d < dm:
                k = p
                dm = d

        ms.append(k)

    px = sum(j[0] for j in ms)/c[t] * h
    py = sum(j[1] for j in ms)/c[t] * h

    print(int(px), int(py))