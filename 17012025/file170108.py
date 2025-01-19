from itertools import *

a = 'АВНРЬЯ'
b = 0
m = 0

for i in product(a, repeat = 5):
    b = b+1
    c = ''.join(i)
    if c[0] != 'Я' and c.count('ЯЯ') == 0 and c.count('Ь') <= 1:
        m = max(m,b)

print(m)