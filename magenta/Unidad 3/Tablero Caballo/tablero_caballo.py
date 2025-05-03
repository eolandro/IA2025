N = 8

movimientosX = [2, 1, -1, -2, -2, -1, 1, 2]
movimientosY = [1, 2, 2, 1, -1, -2, -2, -1]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(['{:2d}'.format(x) for x in fila])

def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

def contar_movimientos(x, y, tablero):
    cuenta = 0
    for i in range(8):
        nx = x + movimientosX[i]
        ny = y + movimientosY[i]
        if es_valido(nx, ny, tablero):
            cuenta += 1
    return cuenta

def siguiente_movimiento(x, y, tablero):
    min_grado = 9
    mejor_mov = (-1, -1)
    for i in range(8):
        nx = x + movimientosX[i]
        ny = y + movimientosY[i]
        if es_valido(nx, ny, tablero):
            grado = contar_movimientos(nx, ny, tablero)
            if grado < min_grado:
                min_grado = grado
                mejor_mov = (nx, ny)
    return mejor_mov

def recorrido_caballo(x, y):
    tablero = [[-1 for _ in range(N)] for _ in range(N)]
    tablero[x][y] = 0

    for paso in range(1, N * N):
        sig = siguiente_movimiento(x, y, tablero)
        if sig == (-1, -1):
            return None  # No hay solución desde esta posición
        x, y = sig
        tablero[x][y] = paso

    return tablero

# ===================== MENÚ PRINCIPAL =====================

print("             PROGRAMA DEL RECORRIDO DEL CABALLO")


# Mostrar tablero de coordenadas para facilitar al usuario
print("Coordenadas del tablero (fila, columna):")
for i in range(N):
    print(['{:2d},{:2d}'.format(i, j) for j in range(N)])
print()

# Entrada del usuario
entrada = input("Ingrese posición inicial (fila,col): ").strip()
try:
    fila, col = map(int, entrada.split(','))
    if 0 <= fila < N and 0 <= col < N:
        resultado = recorrido_caballo(fila, col)
        if resultado:
            print("\n ¡¡Se encontró una solución!!\n")
            imprimir_tablero(resultado)
        else:
            print("\n No se pudo completar el recorrido desde esa posición.")
    else:
        print(" Coordenadas fuera del rango (0–7).")
except:
    print(" Entrada inválida. Usa el formato: fila,col (por ejemplo: 2,3)")
