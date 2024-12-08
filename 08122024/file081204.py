from itertools import *

a = '1357'
b = '2468'

c = 0

for i in product(a, b, a, b, a, b, a, b, a, b, a):

    k = ''.join(i)
    d = 0

    for i in (a + b):

        if k.count(i) > 4:
            d = 1
            break

    if d == 0:
        c = c + 1

print(c * 2)