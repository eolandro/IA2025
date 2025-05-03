mapa_posiciones = {
    1: (0, 0),
    2: (1, 0), 3: (1, 1),
    4: (2, 0), 5: (2, 1), 6: (2, 2),
    7: (3, 0), 8: (3, 1), 9: (3, 2), 10: (3, 3),
    11: (4, 0), 12: (4, 1), 13: (4, 2), 14: (4, 3), 15: (4, 4)
}

def crear_tablero(posicion_vacia):
    tablero = [
        [1],
        [1, 1],
        [1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    x, y = mapa_posiciones[posicion_vacia]
    tablero[x][y] = 0 
    return tablero

def imprimir_tablero(tablero):
    for i, fila in enumerate(tablero):
        print(" " * (4 - i) + " ".join("●" if celda == 1 else "○" for celda in fila))
    print("\n")

def movimiento_valido(tablero, inicio, fin):
    x1, y1 = mapa_posiciones[inicio]
    x2, y2 = mapa_posiciones[fin]
    
    if tablero[x1][y1] == 1 and tablero[x2][y2] == 0:
        if abs(x1 - x2) == 2 and y1 == y2 and tablero[(x1 + x2) // 2][y1] == 1:
            return True
        elif abs(y1 - y2) == 2 and x1 == x2 and tablero[x1][(y1 + y2) // 2] == 1:
            return True
        elif abs(x1 - x2) == 2 and abs(y1 - y2) == 2 and tablero[(x1 + x2) // 2][(y1 + y2) // 2] == 1:
            return True
    return False

def hacer_movimiento(tablero, inicio, fin):
    if movimiento_valido(tablero, inicio, fin):
        x1, y1 = mapa_posiciones[inicio]
        x2, y2 = mapa_posiciones[fin]
        tablero[(x1 + x2) // 2][(y1 + y2) // 2] = 0
        tablero[x2][y2] = 1
        tablero[x1][y1] = 0
        return True
    else:
        return False

def deshacer_movimiento(tablero, inicio, fin):
    x1, y1 = mapa_posiciones[inicio]
    x2, y2 = mapa_posiciones[fin]
    tablero[x1][y1] = 1
    tablero[x2][y2] = 0
    tablero[(x1 + x2) // 2][(y1 + y2) // 2] = 1

def comprobacion_resultado(tablero):
    return sum(sum(fila) for fila in tablero) == 1

def movimientos_comesolos():
    movimientos = []
    for inicio in range(1, 16):
        for fin in range(1, 16):
            if inicio != fin:
                movimientos.append((inicio, fin))
    return movimientos

success = []

def resolver_comesolos(tablero, movimientos_realizados=[], tableros=[]):
    if comprobacion_resultado(tablero):
        print("Solución encontrada con los siguientes movimientos:")
        for mov, t in zip(movimientos_realizados, tableros):
            print(f"Movimiento de punto {mov[0]} a {mov[1]}:")
            imprimir_tablero(t)
        global success
        success = movimientos_realizados.copy()
        return True

    movimientos_posibles = movimientos_comesolos()
    for inicio, fin in movimientos_posibles:
        if hacer_movimiento(tablero, inicio, fin):
            movimientos_realizados.append((inicio, fin))
            tableros.append([fila.copy() for fila in tablero])
            
            print(f"Movimiento de punto {inicio} a {fin}:")
            imprimir_tablero(tablero)
            
            if resolver_comesolos(tablero, movimientos_realizados, tableros):
                return True
            
            deshacer_movimiento(tablero, inicio, fin)
            movimientos_realizados.pop()
            tableros.pop()
            print(f"Retrocediendo movimiento de punto {fin} a {inicio}:")
            imprimir_tablero(tablero)
    
    return False

print("\n⚊⚊⚊⚊⚊⚊✰ COMESOLOS ✰⚊⚊⚊⚊⚊⚊\n")
print("Posiciones del tablero:\n")
contador = 1
for i in range(5):
    fila = []
    for j in range(i + 1):
        fila.append(str(contador).rjust(2))
        contador += 1
    print(" " * (4 - i) + " ".join(fila))
print("\n")

posicion_vacia = int(input("Ingrese la posición vacía inicial (1-15): "))

if posicion_vacia < 1 or posicion_vacia > 15:
    print("La posición debe estar entre 1 y 15.")
else:
    tablero = crear_tablero(posicion_vacia)
    print("\nTablero inicial:")
    imprimir_tablero(tablero)

    if resolver_comesolos(tablero):
        print("¡Comesolos resuelto!")
        print("\nLista de movimientos realizados:")
        for movimiento in success:
            print(f"De {movimiento[0]} a {movimiento[1]}")
    else:
        print("No se encontró una forma válida")