from itertools import *

c = 0
a = 'УОА'
for i in product(a, repeat=6):
    c = c + 1
    b = ''.join(i)
    if b == 'ОУУУОО':
        print(c, b)