import time

def es_movimiento_valido(x, y, tablero, n):
    """Verifica si el movimiento está dentro del tablero y la casilla no ha sido visitada"""
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1

def contar_movimientos_posibles(x, y, tablero, n, movimientos_x, movimientos_y):
    """Cuenta cuántos movimientos posibles hay desde una posición dada"""
    count = 0
    for i in range(8):
        next_x = x + movimientos_x[i]
        next_y = y + movimientos_y[i]
        if es_movimiento_valido(next_x, next_y, tablero, n):
            count += 1
    return count

def siguiente_movimiento(x, y, tablero, n, movimientos_x, movimientos_y):
    """Selecciona el siguiente movimiento según la regla de Warnsdorff"""
    min_degree = 9
    min_index = -1
    
    for i in range(8):
        next_x = x + movimientos_x[i]
        next_y = y + movimientos_y[i]
        if es_movimiento_valido(next_x, next_y, tablero, n):
            degree = contar_movimientos_posibles(next_x, next_y, tablero, n, movimientos_x, movimientos_y)
            if degree < min_degree:
                min_degree = degree
                min_index = i
    
    if min_index == -1:
        return -1, -1
    
    next_x = x + movimientos_x[min_index]
    next_y = y + movimientos_y[min_index]
    
    return next_x, next_y

def imprimir_tablero(tablero, n, paso, delay=0.5):
    """Imprime el tablero con el recorrido actual"""
    print(f"\nPaso {paso}:")
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == -1:
                print("  .", end=" ")
            else:
                print(f"{tablero[i][j]:3}", end=" ")
        print()
    time.sleep(delay)

def encontrar_recorrido(n, inicio_x, inicio_y, delay=0.5):
    """Encuentra el recorrido del caballo mostrando cada paso"""
    tablero = [[-1 for _ in range(n)] for _ in range(n)]
    movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    x, y = inicio_x, inicio_y
    tablero[x][y] = 1
    imprimir_tablero(tablero, n, 1, delay)
    
    for paso in range(2, n*n + 1):
        next_x, next_y = siguiente_movimiento(x, y, tablero, n, movimientos_x, movimientos_y)
        if next_x == -1 and next_y == -1:
            print("\nNo hay movimientos válidos disponibles.")
            return False, tablero
        
        x, y = next_x, next_y
        tablero[x][y] = paso
        imprimir_tablero(tablero, n, paso, delay)
    
    return True, tablero

def main():
    print("Recorrido del Caballo en Ajedrez - Visualización Paso a Paso")
    print("-----------------------------------------------------------")
    
    n = 8  # Tamaño del tablero
    
    # Solicitar posición inicial
    while True:
        try:
            print(f"\nIngrese la posición inicial (fila y columna, 0-{n-1})")
            inicio_x = int(input("Fila (0-7): "))
            inicio_y = int(input("Columna (0-7): "))
            
            if 0 <= inicio_x < n and 0 <= inicio_y < n:
                break
            else:
                print(f"Por favor ingrese valores entre 0 y {n-1}.")
        except ValueError:
            print("Por favor ingrese números enteros válidos.")
    
    # Configurar velocidad de visualización
    delay = float(input("\nIngrese el tiempo de pausa entre pasos (segundos, ej. 0.5): "))
    
    # Encontrar y mostrar el recorrido
    exito, tablero = encontrar_recorrido(n, inicio_x, inicio_y, delay)
    
    if exito:
        print("\n¡Recorrido completo encontrado!")
    else:
        print("\nSolo se encontró un recorrido parcial.")

if __name__ == "__main__":
    main()