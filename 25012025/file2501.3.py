files = ['27a3.txt', '27b3.txt']
c = [2, 6]
h = 10000

def zxc(p, t):
    x, y = p
    if t == 0:
        if (2 < y) or (-2 < x < (-1.6) and -4 < y < -2) or ((3.6) < x < (4.4) and -4 < y < (-3.2)) or ((12.4) < x and (-1.2) < y):
            return 6
        return (y < -x)
    if y > 1.2*x + 12:
        return 5
    if y > 0.8*x + 4:
        return y > 7
    if y > 3.9:
        return 4
    return ((y>x-2)+2)


def fye(a, b):
    x1, y1 = a
    x2, y2 = b

    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


for t in range(2):
    fo = open(str(files[t]))
    fo.readline()
    cs = [[], [], [], [], [], [], []]
    n = c[t]

    for line in fo:
        p = [float(d) for d in line.replace(',', '.').split()]
        if
            u = zxc(p, t)
            cs[u].append(p)

    ms = []

    for i in range(n):
        dm = 0
        k = [0,0]

        for p in cs[i]:
            d = sum(fye(p, j) for j in cs[i])
            if d > dm:
                k = p
                dm = d

        ms.append(k)


    px = sum(j[0] for j in ms)/c[t] * h
    py = sum(j[1] for j in ms)/c[t] * h

    print(int(px), int(py))