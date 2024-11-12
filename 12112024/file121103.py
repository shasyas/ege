f = open('1_26.txt')

a = []

def cake(n, ck):
    c = a[n]
    m = 0
    if n < len(a)-2:
        if a[n+1] > c+3:
            m = n+1
        elif n < len(a)-3:
            if a[n+2] > c+3:
                m = n+2
            elif n < len(a)-4:
                if a[n+3] > c+3:
                    m = n+3
                elif n < len(a)-5:
                    m = n+4
    if m > 0:
        return (m, (cake(m, 1)[1] + ck))
    else:
        return ((n), (1))

for i in range(10000):
    b = int(f.readline())
    if b not in a:
        a.append(b)
a.sort()
mn = cake(0,1)
mx = 0
for i in range(len(a)):
    if cake(i,1) == mn:
        mx = i
print(mn[1], a[mx])