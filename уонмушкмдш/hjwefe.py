from itertools import *

def bkb():

    def f(x,y,z,w,u):
        return ((z<=w)and(y!=x))<=(u==(y or z))

    for a1, a2, a3, a4, a5, a6, a7, a8 in product([0,1], repeat = 8):
        tab = [(0,a1,0,0,0), (0,a2,a3,0,0), (a4,0,0,0,a5), (0,0,a6,a7,a8)]

        if len(tab) == len(set(tab)):
            for p in permutations('xyzwu'):
                if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0, 0]:
                    print(p)

bkb()