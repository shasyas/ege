#M=842x5 9, N=8x725 9

m = 5 + 81*2 + 81*9*4 + 8*81*81
n = 5 + 9*2 + 81*7 + 81*81*8

for a in range(10000):
    for x in range(9):
        if (a + m + x*9)%(x*9*81 + n) == 0:
            print(a)
