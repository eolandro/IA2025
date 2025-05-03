N = 4  # Tamaño del tablero
R = 4  # Número de reinas a colocar

tab = [['.' for _ in range(N)] for _ in range(N)]
reinas_r = R

def es_valido(tab, fila, col):
    for i in range(fila):
        if tab[i][col] == 'R':
            return False
        if col - (fila - i) >= 0 and tab[i][col - (fila - i)] == 'R':
            return False
        if col + (fila - i) < N and tab[i][col + (fila - i)] == 'R':
            return False
    return True

def colocar_reinas(tab):
    global reinas_r
    for fila in range(N):
        for col in range(N):
            if es_valido(tab, fila, col):
                tab[fila][col] = 'R'
                reinas_r -= 1
                print(f"\nReina colocada en fila {fila + 1}, columna {col + 1}")
                print(f"Reinas restantes: {reinas_r}")
                imprimir_tablero(tab)
                if reinas_r == 0:
                    return True
                break
    return False

def imprimir_tablero(tab):
    print("  +" + "--" * N + "+")
    for fila in tab:
        print("  | " + ' '.join(fila) + " |")
    print("  +" + "--" * N + "+\n")

# Colocar las reinas

print("║    Posicion de Reinas    ║")


colocar_reinas(tab)

# Mostrar el resultado final
print(" Tablero final:")
imprimir_tablero(tab)
