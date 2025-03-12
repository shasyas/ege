f = open('17.txt')

a = []
m = 0
k = []

for i in range(6633):
    b = int(f.readline())
    a.append(b)
    if b%1000 == 321:
        m = max(m,b)

for i in range(2,6633):
    c = 0
    d = 0
    for j in range(3):
        if a[i-j] > 9999:
            c = c+1
        if a[i-j]%5 == 0:
            d = 1
    if c == 2 and d == 1 and (a[i-2] + a[i-1] + a[i]) > m:
        k.append(a[i-2] + a[i-1] + a[i])

print(len(k), max(k))