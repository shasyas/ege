from itertools import product


a = '10A'
b = 0


for i in product(a, repeat=8):
    k = "".join(i)
    if (k.count('A') <= 4) and (k.count('0') == 2) and (k[0] != '0'):
        b = b + (9**k.count('1'))*(6**k.count('A'))
print(b)