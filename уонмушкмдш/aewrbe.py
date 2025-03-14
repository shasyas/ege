from bs4 import BeautifulSoup
from random import *

soup = BeautifulSoup('<html><head><title>Заголовок страницы</title></head><body></body></html>', 'html.parser')

# Получаем тег body и добавляем в него параграф
soup.body.append(soup.new_tag('p', id='intro'))
soup.body.p.string = 'Добро пожаловать на мою страницу!'

print(soup.prettify())

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