f = open('27-A (1).txt')

a = int(f.readline())
b = []

for i in range(a):
    b.append(int(f.readline()))

mx = 0

for i in range(len(b)):

    for j in range(i + 1, len(b)):

        for k in range(j + 1, len(b)):

            if (b[i] + b[j] + b[k]) % 102 == 0:
                mx = max(mx, b[i] + b[j] + b[k])

print(mx)