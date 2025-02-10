#194257368

def fye(n):
    if n < 9:
        return n
    else:
        return fye(n%9) + fye(n//9)

a = 0

for i in range(4*(6**20), 5*(6**20)):
    if fye(i) == 121:
        a = a + 1

print(a)