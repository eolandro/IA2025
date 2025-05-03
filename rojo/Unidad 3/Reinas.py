def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("♕" if celda == 1 else "□" for celda in fila))
    print()

def es_seguro(tablero, fila, col):
    # * Verificación a la izquierda
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
    print(f"\n⚊⚊✰ Procesando Columna {col + 1} ✰⚊⚊")
    
    if col >= 4:
        copia_tablero = [fila[:] for fila in tablero]
        answers.append(copia_tablero)
        print("¡Solución completa encontrada!")
        imprimir_tablero(tablero)
        return True
    
    res = False
    for i in range(4):
        if es_seguro(tablero, i, col):
            print(f"Colocando reina en fila {i + 1}, columna {col + 1}")
            tablero[i][col] = 1
            imprimir_tablero(tablero)
            
            res = resolver_4_reinas(tablero, col + 1, answers) or res
            
            print(f"Retirando reina de fila {i + 1}, columna {col + 1}")
            tablero[i][col] = 0
            imprimir_tablero(tablero)
    
    return res

tablero = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
answers = []

print("\nTablero inicial:")
imprimir_tablero(tablero)

resolver_4_reinas(tablero, 0, answers)

# * Imprimiendo las soluciones
if not answers:
    print("No se encontraron soluciones.")
else:
    print(f"\nSe encontraron {len(answers)} soluciones válidas:")
    for i, solucion in enumerate(answers, 1):
        print(f"\nSolución {i}:")
        imprimir_tablero(solucion)