def mostrar_tablero(tablero):
    for fila in tablero:
        print(f"[{', '.join(fila)}]")  

def movimientos_reina(tablero, fila, col):
    movimientos = []
    for i in range(4):
        for j in range(4):
            if i == fila or j == col or abs(fila - i) == abs(col - j):
                if tablero[i][j] == '':  
                    movimientos.append((i, j))
    return movimientos

def es_seguro(tablero, fila, col):
    for i in range(4):
        for j in range(4):
            if (tablero[i][j] == 'Q' and (i == fila or j == col or abs(fila - i) == abs(col - j))):
                return False
    return True

def colocar_reinas(tablero, reinas_colocadas, contador, inicio_fila=0, inicio_col=0):
    if contador == 0:
        return True

    for i in range(inicio_fila, 4):
        for j in range(inicio_col, 4):
            if tablero[i][j] == '' and es_seguro(tablero, i, j):
                tablero[i][j] = 'Q'
                print(f"Reina {5 - contador} colocada en ({i}, {j})")
                
                movimientos = movimientos_reina(tablero, i, j)
                for x, y in movimientos:
                    tablero[x][y] = 'x'
                
                mostrar_tablero(tablero)  
                
                if contador > 1:
                    input("Presiona Enter para colocar la siguiente reina...")

                if colocar_reinas(tablero, reinas_colocadas + 1, contador - 1):
                    return True

                tablero[i][j] = ''
                for x, y in movimientos:
                    tablero[x][y] = ''

        if i == 3 and j == 3:
            print("No se puede colocar la reina. Reiniciando desde la siguiente casilla.")
            return colocar_reinas([['' for _ in range(4)] for _ in range(4)], 0, 4, 0, 1) 

    return False

def resolver_tablero():
    tablero = [['' for _ in range(4)] for _ in range(4)] 
    if not colocar_reinas(tablero, 0, 4):
        print("No se pudo encontrar una solución")
    else:
        print("¡Solución encontrada!")

resolver_tablero()
