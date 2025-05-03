import time
from collections import deque

tablero_orig = [['🔸'] * 3 for x in range(3)]  # Cambiar espacios en blanco por heno

## Imprime el tablero
def tablero():
    tablero_c = [a.copy() for a in tablero_orig]
    for a in inicio:
        tablero_c[a[1][0]][a[1][1]] = a[0]
    print()
    for fila in tablero_c:
        print(" ".join(map(str, fila)))
    print('\n')

def mover(f, c):
    if f == 0:
        if c < 2:
            return f + c + 1, 2
        else:
            return 2, c - 1
    elif f == 2:
        if c < 2:
            return 0, f - c - 1
        else:
            return f - 1, 0
    elif f == 1:
        if c == 0:
            return 0, 2
        else:
            return 2, 0

inicio = [
    ["♘ ", (0, 0)],
    ["♘ ", (0, 2)],
    ["♞ ", (2, 0)],
    ["♞ ", (2, 2)],
]

final = [
    ['♘ ', (2, 2)], 
    ['♘ ', (2, 0)], 
    ['♞ ', (0, 2)], 
    ['♞ ', (0, 0)]
]

tablero()
while True:
    if inicio == final:
        break
    for a in inicio:
        a[1] = mover(a[1][0], a[1][1])
        print(inicio)
        tablero()