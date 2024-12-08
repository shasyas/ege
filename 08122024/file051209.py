a = open('171.txt').read().split()

f = []
c = 0

mx = 0
mxx = 0

for i in range(len(a)):

    a[i] = int(a[i])

    if a[i] % 100 == 17:
        mx = max(a[i], mx)

for i in range(2, len(a)):
    b = str(a[i - 2] % 5) + str(a[i - 1] % 5) + str(a[i] % 5)
    d = 0
    for j in [a[i - 2], a[i - 1], a[i]]:
        if 10000 > j > 999:
            d = d + 1

    if b.count('0') > 0 and d == 2 and (a[i - 2] + a[i - 1] + a[i] > mx):
        c = c + 1
        mxx = max(mxx, a[i - 2] + a[i - 1] + a[i])


print(mxx, c)