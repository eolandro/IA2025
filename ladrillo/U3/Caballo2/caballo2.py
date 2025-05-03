# Utiliza la regla de Warnsdorff para resolver el problema del recorrido del caballo en un tablero de ajedrez.

# Regla de Warnsdorff:
# 1. El caballo puede iniciar desde cualquier posición en el tablero.
# 2. El caballo se mueve siempre a la posición adyacente y no visitada con menor grado (menor número de posiciones adyacentes no visitadas).
# Definiciones:
# * Una posición Q es accesible desde una posición P si el caballo puede moverse a Q en un solo movimiento y Q no ha sido visitada.
# * La accesibilidad de una posición P es el número de posiciones accesibles desde P.

"""
[0,0,0,0,0,0,0,0] 8 0
[0,0,0,0,0,0,0,0] 7 1
[0,0,0,0,0,0,0,0] 6 2
[0,0,0,0,0,0,0,0] 5 3
[0,0,0,0,0,0,0,0] 4 4
[0,0,0,0,0,0,0,0] 3 5
[0,0,0,0,0,0,0,0] 2 6
[0,0,0,0,0,0,0,0] 1 7
 A B C D E F G H
 0 1 2 3 4 5 6 7
"""

import sys
import time

sys.setrecursionlimit(20000)
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
tablero = [[0 for _ in range(8)] for _ in range(8)]

# Función que genera los movimientos posibles del caballo
# Parámetros:
#   c: Columna en base cero
#   f: Fila en base cero
#   ban: Bandera para activar la heurística
# Retorna:
#   mov: Lista con las posiciones a las que el caballo puede moverse que aún no han sido recorridas
def genPosicion(c, f, ban):
    mov = []
    rangoMovimiento = [[1, -2], [-1, -2], [2, -1], [-2, -1],
                       [2, 1], [-2, 1], [1, 2], [-1, 2]]
    for i in rangoMovimiento:
        nx, ny = c + i[0], f + i[1]
        if (0 <= nx < 8) and (0 <= ny < 8) and tablero[ny][nx] == 0:
            mov.append([nx, ny])
    
    if mov and ban:
        access = [len(genPosicion(m[0], m[1], False)) for m in mov]
        # Ordena los movimientos posibles según la regla de Warnsdorff
        mov = [x for _, x in sorted(zip(access, mov))]
    
    return mov

# Función de recorrido backtracking
# Parámetros:
#   p: Columna en base cero
#   q: Fila en base cero
#   contador: Número de casillas recorridas
# Retorna:
#   1: Si se logró recorrer todo el tablero
#   2: Si no hay más caminos posibles
def recorrido(p, q, contador):
    tablero[q][p] = contador  # Coloca el contador en la posición actual
    contador += 1

    if contador == 65:  # Se ha recorrido todo el tablero (64 casillas + 1)
        # Imprimir el tablero completo y retornar 1
        for i, a in enumerate(tablero):
            fila = ['{:>3}'.format(b) for b in a]
            print(8 - i, ' ', *fila, '\n')
        print('      A   B   C   D   E   F   G   H\n\n')
        return 1
    else:
        # Obtener lista de posibles movimientos a partir de la posición actual
        pos = genPosicion(p, q, True)
        if pos:
            for po in pos:
                # Intentar recorrido a través de 'po'. Guardar retorno en 'ban'
                ban = recorrido(po[0], po[1], contador)
                if ban == 1:
                    # El recorrido a través de 'po' fue exitoso, retornar 1
                    return 1
    
    # Se llega a esta parte del código si:
    #   No se encontró un camino exitoso
    # Reiniciar la posición actual (retroceso)
    tablero[q][p] = 0
    return 2

# Inicio del programa
print('*** Recorrido del Caballo Ajedrez ***\n\n')
for i, a in enumerate(tablero):
    fila = ['{:>2}'.format(b) for b in a]
    print(8 - i, ' ', *fila)
print('\n     A  B  C  D  E  F  G  H\n\n')

# Obtener y guardar coordenadas dentro de coord
while True:
    print("Ingrese en coordenadas de ajedrez la casilla inicial del caballo (sugerencia: A8)")
    coord = input(">: ").upper()
    if (len(coord) == 2) and (coord[0] in letras) and (1 <= int(coord[1]) <= 8):
        break
    print("Formato incorrecto")

tiempo = time.time()
print("Procesando... Espere por favor \n")

# Convertir la coordenada en ajedrez a los índices correspondientes en el tablero
R = recorrido(letras.index(coord[0]), 8 - int(coord[1]), 1)  # Iniciar contador en 1
if R == 1:
    print(f"Se encontró la solución en {time.time() - tiempo:.4f} segundos")
else:
    print(f"Acabas de perder {time.time() - tiempo:.4f} segundos de tu vida en esto")