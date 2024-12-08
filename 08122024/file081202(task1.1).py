a = "15 17 18 24 27 28 34 35 37 42 43 47 51 53 56 65 68 71 72 73 74 81 82 86"
g = "АБ АГ АЕ БА БГ БВ ВБ ВД ВИ ГА ГБ ГЕ ДВ ДЖ ЕА ЕГ ЕЖ ЖЕ ЖД ЖИ ИВ ИЖ"

b = a.split()
c = a


def wrk(t, k):
    s = set(g.replace(' ', ''))
    for p in permutations(s):
        nt = t
        for i, v in enumerate(p):
            nt = nt.replace(str(i + 1), v)
        if set(g.split()) == set(nt.split()):
            print(p, k)
            return


for i in b:
    c = c.replace(str(i), '')
    c = c.replace(i[::-1], '')
    wrk(c, i)
    c = a
