def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("♕" if celda == 1 else "□" for celda in fila))
    print()

def es_seguro(tablero, fila, col):
    # * Verificación a la zquierda
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    
    # * Verificación diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # * Verificación diagonal inferior izquierda
    for i, j in zip(range(fila, 4, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_4_reinas(tablero, col, answers):
    if col >= 4:
        copia_tablero = [fila[:] for fila in tablero]
        answers.append(copia_tablero)
        return True
    
    res = False
    for i in range(4):
        if es_seguro(tablero, i, col):
            tablero[i][col] = 1
            res = resolver_4_reinas(tablero, col + 1, answers) or res
            tablero[i][col] = 0  # ! Backtrack
    
    return res

tablero = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
answers = []

print("\nEn el siguiente tablero:\n")
for fila in tablero:
    print(" ".join("♕" if celda == 1 else "□" for celda in fila))
    
resolver_4_reinas(tablero, 0, answers)

if not answers:
    print("No se encontraron soluciones.")
else:
    print(f"\nSe encontraron {len(answers)} soluciones para colocar las 4 reinas:\n")
    for i, solucion in enumerate(answers, 1):
        print(f"Solución {i}:")
        imprimir_tablero(solucion)