# Definición del tablero y variables
tablero_inicial = [['👽'] * 4 for _ in range(4)]
reina = '👑'
casilla_atacada = '⬛'
soluciones = []

def copiar_tablero(tablero):
    return [fila.copy() for fila in tablero]

def imprimir_tablero(tablero):
    for fila_tablero in tablero:
        print(" ".join(fila_tablero))
    print("\n")

def marcar_casillas_atacadas(tablero, y, x):
    # Marcar columna y fila
    for fc in range(4):
        tablero[fc][x] = casilla_atacada
        tablero[y][fc] = casilla_atacada

    # Marcar diagonal descendente
    for d in range(-3, 4):
        if 0 <= y + d < 4 and 0 <= x + d < 4:
            tablero[y + d][x + d] = casilla_atacada

    # Marcar diagonal ascendente
    for d in range(-3, 4):
        if 0 <= y - d < 4 and 0 <= x + d < 4:
            tablero[y - d][x + d] = casilla_atacada

    # Colocar la reina en la posición actual
    tablero[y][x] = reina

def resolver(tablero, fila, reinas):
    if reinas == 4:
        # Guardar una copia de la solución encontrada
        soluciones.append(copiar_tablero(tablero))
        print("Solución encontrada:")
        imprimir_tablero(tablero)
        return

    for columna in range(4):
        if tablero[fila][columna] == '👽':  # Solo considerar casillas sin atacar
            # Hacer una copia del tablero antes de marcar casillas
            tablero_copia = copiar_tablero(tablero)
            marcar_casillas_atacadas(tablero_copia, fila, columna)
            
            # Mostrar el tablero después de colocar cada reina
            print(f"Paso a paso - Colocando reina en: ({fila}, {columna})")
            imprimir_tablero(tablero_copia)
            
            # Llamada recursiva para la siguiente fila
            resolver(tablero_copia, fila + 1, reinas + 1)

# Inicializar la resolución desde la primera fila
resolver(tablero_inicial, 0, 0)

# Imprimir todas las soluciones encontradas
print("Resumen de todas las configuraciones posibles para colocar 4 reinas en un tablero de 4x4 sin que se ataquen:")
for idx, solucion in enumerate(soluciones, start=1):
    print(f"Solución {idx}:")
    imprimir_tablero(solucion)