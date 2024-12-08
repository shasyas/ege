f = open('27-A.txt')

a = int(f.readline())
b = []

for i in range(a):
    b.append(int(f.readline()))

mn = 10 ** 10

for i in range(len(b)):

    for j in range(i + 1, len(b)):

        for k in range(j + 1, len(b)):

            if b[i] < b[j] < b[k]:
                mn = min(mn, b[i] + b[j] + b[k])

print(mn)