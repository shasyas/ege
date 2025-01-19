f = open('24.txt')

a = f.read().split('FSRQ')

m = 0
n = 0

for i in range(81):
    n = n + len(a[i]) + 4

n = n-1

m = n

n = n - len(a[0]) + len(a[81]) + 3

for i in range(82,len(a)):
    n = n - len(a[i-81]) + len(a[i])
    m = max(m, n)

print(m)