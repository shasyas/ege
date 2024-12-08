def heh(x):
    c = x * 4 + x % 3

    return c * 8 + c % 5


a = 1111111110 // 32 - 5
b = 1444444416 // 32 - 5

while heh(a) < 1111111110:
    a = a + 1

while heh(b) <= 1444444416:
    b = b + 1

print(b - a)