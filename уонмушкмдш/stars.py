from random import *

a = ['.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '----', '--.-', '.--.-.', '-.--', '-..-', '...-...', '..--', '.-.-']
f = ['░', '◌']
h = ['▤', '◍']
#1072

def ch(x):
    if x == '.':
        return choice(f)
    else:
        return choice(h)

def sim(c):
    if 1072 > ord(c) > 1039:
        c = chr(ord(c) + 32)
    if (ord(c) > 1103) or (ord(c) < 1072):
        return c
    b = a[ord(c)-1072]
    d = ''
    for i in b:
        d = d + ch(i)
    return d + '☆'

def lt(n):
    m = ''
    for j in n:
        m = m + sim(j)
    if m[-1] == '☆':
        return m[:-1]
    else:
        return m

print(lt('спокойной ночи'))