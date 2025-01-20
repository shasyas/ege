f = open('24.txt').read().split('C')

b = []
a = []

for i in range(len(f)):
    c = f[i].split('AA')
    for j in c:
        b.append(j)

for i in range(len(f)):
    c = b[i].split('BB')
    for j in c:
        a.append(j)



for i in range(len(a)):
    if a[i] != '' and a[i][0] == 'A':
        a[i] = len(a[i])
    else:
        a[i] = 0

print(max(a))