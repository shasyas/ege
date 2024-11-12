def hm(n):
    a = str(bin(n))[2::]
    if a[-1] == '0':
        a = '11' + a
    else:
        a = '1' + a + '10'
    return int(a, 2)


n = 0
m = hm(123456789)
mn = 123456789

for i in range(380000000, 456789013):
    if hm(i) > m:
        m = hm(i)
        mn = i

print(m, mn)