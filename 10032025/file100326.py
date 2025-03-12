f = open('26.txt')

a = []
n = int(f.readline())

for i in f:
    s, t, w = [int(j) for j in i.split()]
    a.append([s, t, w])

a.sort()

w1 = []
w2 = []
c = 0
d = 0

for s, t, w in a:

    while len(w1) > 0 and w1[0] <= s:
        del w1[0]
    while len(w2) > 0 and w2[0] <= s:
        del w2[0]
    if w == 1 or (w != 1 and w != 2 and len(w1) <= len(w2)):
        if len(w1) == 0:
            w1.append(s + t)
        elif len(w1) < 14:
            w1.append(w1[-1] + t)
        else:
            d += 1
    else:
        if len(w2) == 0:
            c += 1
            w2.append(s + t)
        elif len(w2) < 14:
            w2.append(w2[-1] + t)
            c += 1
        else:
            d += 1
print(c, d)