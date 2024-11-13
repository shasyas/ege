f = open('241.txt')
s = f.readline()
a = s.split('CD')

m = 0
n = 0

m = len(''.join(a[i:i + 141])) + 140 * 2

for i in range(1, len(a) - 141):
    n = len(''.join(a[i:i + 141])) + 141 * 2
    if n > m:
        m = n

print(m)