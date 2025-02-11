#24
a = open('27-B.txt')
s = int(a.readline())
m = []
n = []
k = []

for j in range(s):

    i = a.readline()

    if int(i)%3 == 0:
        m.append(int(i))

    if int(i)%3 == 1:
        n.append(int(i))

    if int(i)%3 == 2:
        k.append(int(i))

m.sort()
n.sort()
k.sort()
print(n)
b = [(m[0]+n[0]+k[0]), (m[0]+m[1]+m[2]), (n[0]+n[1]+n[2]), (k[0]+k[1]+k[2])]
print(min(b))