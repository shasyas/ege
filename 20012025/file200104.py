f = open('17.txt')

a = 0
b = []
m = 0

for i in range(5542):
    e = int(f.readline())
    b.append(e)

for k in range(5541):
    i = b[k]
    j = b[k+1]
    if (i+j)%7 == 0 and (i*j)%15 == 0:
        a = a + 1
        m = max(m, i+j)

print(a, m)