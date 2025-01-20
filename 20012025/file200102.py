from itertools import *

a = '0123456'
b = 0

for i in product(a, repeat=4):
    if i[0] != 0 and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]):
        b = b + 1

print(b)