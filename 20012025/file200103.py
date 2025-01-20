a = 5**15 + 5**18 - 30
b = a
c = ''

while b > 0:
    c = c + str(b%5)
    b = b//5

print(c)