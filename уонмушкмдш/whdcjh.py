f = open('17.txt')

a = []
c = 0
d = []

for i in range(9929):
    b = int(f.readline())
    a.append(b)

mn = min(a) % 3
mx = max(a) % 7

for i in range(len(a) - 1):
    if (((a[i] % 3 == mn) or (a[i + 1] % 3 == mn)) and ((a[i] % 7 == mx) or (a[i + 1] % 7 == mx))):
        c = c + 1
        d.append(a[i] + a[i + 1])

print(c, max(d))