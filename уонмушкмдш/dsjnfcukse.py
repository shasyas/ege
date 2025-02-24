a = (9**4)*2 + (9**2)*6 + 9*6 + 1
b = 0

#2y66x 9+x0y1 12
#

for x in range(9):
    for y in range(9):
        b = (12**3 + 1)*x + (9**3 + 12)*y
        if (a+b)%170 == 0:
            print(x,y, (a+b)/170)