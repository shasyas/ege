f = open('27_A.txt')
a = int(f.readline())

b = []
m = 10000000
for i in range(a):
    b.append(int(f.readline()))

for i in range(a):
    n = 0
    for j in range(a):
        n = n + b[j]*min((abs(j-i)), (a-abs(j-i)))
    m = min(m,n)

print(m*3)