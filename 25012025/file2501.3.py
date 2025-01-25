files = ['27a3.txt', '27b3.txt']
c = [2, 6]
h = 10000

def zxc(p, t):
    x, y = p
    if t == 0:
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

    if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 > 1:
        return (0,((x1 - x2)**2 + (y1 - y2)**2)**0.5)

    return (1,((x1 - x2)**2 + (y1 - y2)**2)**0.5)


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
        dm = 1

        for p in cs[i]:
            d = sum(fye(p, j)[1] for j in cs[i])
            g = sum(fye(p, j)[0] for j in cs[i])
            if d > dm and g > 0:
                k = p
                dm = d

        ms.append(k)

    px = sum(j[0] for j in ms)/c[t] * h
    py = sum(j[1] for j in ms)/c[t] * h

    print(int(px), int(py))