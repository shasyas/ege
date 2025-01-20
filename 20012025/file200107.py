a = 7718
b = []
c = 0
m = 0

f = open('26.txt')

for i in range(2810):
    b.append(int(f.readline()))

b.sort()

for j in range(len(b)):
    i = b[j]
    if a > i:
        a = a-i
        c = c + 1
    else:
        a = a + b[j-1]
        break

for i in b:
    if a > i:
        m = max(m,i)


print(c,m)