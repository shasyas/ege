from itertools import *

b = 0

a = ['А', 'Д', 'Е', 'Й', 'Н', 'Р']
for i in product(a, repeat=6):
    c = ''.join(i)
    if c.count('А') > 0 and c.count('Й') < 2:
        b = b + 1

print(b)