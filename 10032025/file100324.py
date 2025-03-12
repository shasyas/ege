f = open('24.txt')
a = f.readline().split('F')

m = 0
n = 0

for i in a:
    if i.count('A') <3:
        n = n + len(i)+1
        m = max(m, n+1)
    else:
        n = 0

print(m)