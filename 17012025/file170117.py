f = open('17.txt')

m = 0
c = []
n = []

for i in range(10000):
    a = int(f.readline())
    c.append(a)
    if ((a > 9999) or (a <- 9999)) and (a%100 == 43):
        m = max(a,m)

for i in range(len(c)):
    if ((c[i] > 9999) and (c[i]%100 == 43)) or ((c[i] <- 9999) and (c[i]%100 == 57)):
        if (c[i-2]**2 + c[i-1]**2 + c[i]**2) <= m**2:
            n.append((c[i-2]**2 + c[i-1]**2 + c[i]**2))

        if (c[i-1]**2 + c[i]**2 + c[i+1]**2) <= m**2:
            n.append(c[i-1]**2 + c[i]**2 + c[i+1]**2)

        if (c[i]**2 + c[i+2]**2 + c[i+1]**2) <= m**2:
            n.append(c[i]**2 + c[i+2]**2 + c[i+1]**2)

print(len(n), min(n))

