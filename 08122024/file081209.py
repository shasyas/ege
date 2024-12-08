f = open('263.txt')

a = f.readline()

b = [0] * 86400
c = 0

for i in f:

    p, q = map(int, i.split())

    for j in range(p, q):
        b[j] = b[j] + 1

c = max(b[8 * 60 * 60:14 * 60 * 60 + 1])

r = b[8 * 60 * 60:14 * 60 * 60 + 1].count(c)

print(c, r)