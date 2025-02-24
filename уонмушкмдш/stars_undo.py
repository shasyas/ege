codes = ['.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '----', '--.-', '.--.-.', '-.--', '-..-', '...-...', '..--', '.-.-']
dots = ['░', '◌']
lines = ['▤', '◍']

def morse(x):

    if x in dots:
        return '.'
    elif x in lines:
        return '-'
    else:
        return x


def msim(coded_piece):
    lettr = ''
    piece = ''
    for i in coded_piece:
        piece = piece + morse(i)
    if piece == '':
        return ' '
    if piece[0] == ' ':
        lettr = ' '
        piece = piece[1:]
    lettr = lettr + chr(codes.index(piece) + 1072)
    return lettr

def decoder(simbl):
    simbl = simbl.split('☆')
    m_simbl = ''
    for j in simbl:
        m_simbl = m_simbl + msim(j)
    return m_simbl

#print(decoder('◌░◌☆◌▤◍◌☆▤▤◍☆▤◌▤☆◍◍▤☆░◍◍▤☆◍░☆▤◍◍☆░▤▤▤☆ ◍◌☆▤▤▤☆▤◍◍◌☆░◌'))

print(decoder('░◌░◌☆◍▤◍☆◍▤▤◌☆░◌▤☆ ◍◍░░☆░▤☆◌▤▤☆░▤☆◌◍░☆◌░☆◍☆▤░░◍☆ ◌◌◍☆◍◍▤◍☆◌░☆ ◍◍☆◍◍▤☆◍◌☆◍☆◌▤☆◌◌◌▤☆▤◌☆◍◍◍☆░◍▤◍☆ ◌▤◍◌☆░☆▤◌☆▤▤▤☆◌◍▤▤'))