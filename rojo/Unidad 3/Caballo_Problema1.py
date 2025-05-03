import time

# Tablero inicial junto con las posiciones
tablero = [
    ['♞', '□', '♞'],
    ['□', '□', '□'],
    ['♘', '□', '♘']
]
posiciones = {
    'CN1': (0, 0),
    'CN2': (0, 2),
    'CB1': (2, 0),
    'CB2': (2, 2)
}

# Movimientos posibles siguiendo las manecillas del reloj
movimientos_reloj = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def imprime():
    for fila in tablero:
        print(" ".join(fila))
    print("⚊⚊⚊⚊⚊⚊✰⛤✰⚊⚊⚊⚊⚊⚊")

def mover_caballo(nombre):
    x, y = posiciones[nombre]
    for dx, dy in movimientos_reloj:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3 and tablero[nx][ny] == '□':
            tablero[x][y] = '□'
            if nombre.startswith('CB'):
                tablero[nx][ny] = '♘'
            else:
                tablero[nx][ny] = '♞'
            posiciones[nombre] = (nx, ny)
            imprime()
            time.sleep(0.5)
            return True
    return False

# Tablero deseado
def juego_completo():
    return tablero == [
        ['♘', '□', '♘'],
        ['□', '□', '□'],
        ['♞', '□', '♞']
    ]

print("Tablero Inicial:")
imprime()

orden_caballos = ['CN2', 'CB2', 'CB1', 'CN1']

# Solución del juego
resuelto = False
while not resuelto:
    for caballo in orden_caballos:
        mover_caballo(caballo)
        if juego_completo():
            resuelto = True
            break

print("Tablero Final:")
imprime()