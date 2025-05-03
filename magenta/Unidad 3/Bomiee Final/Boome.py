import heapq
import os
from ruamel.yaml import YAML

# Función para cargar el tablero desde el archivo YAML
def cargar_tablero():
    yaml = YAML()
    with open("tablero.yaml", "r") as archivo:
        return yaml.load(archivo)['matriz']

# Definir los movimientos posibles (incluyendo diagonales)
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Función para verificar si una celda es válida
def es_valida(x, y, m):
    return 0 <= x < len(m) and 0 <= y < len(m[0]) and 'X' not in m[x][y]

# Función para obtener las posiciones de inicio y fin
def obtener_puntos(m):
    inicio = fin = None
    for i, fila in enumerate(m):
        for j, celda in enumerate(fila):
            if 'B' in celda:
                inicio = (i, j)
            elif '0' in celda:
                fin = (i, j)
    return inicio, fin

# Heurística: distancia Manhattan
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Algoritmo de búsqueda del camino (A* con optimización de Dijkstra)
def encontrar_camino(m, r_dijk=5):
    inicio, fin = obtener_puntos(m)
    if not inicio or not fin:
        return None

    abierta = [(heuristica(inicio, fin), 0, inicio)]  # Prioridad: (f, g, nodo)
    de_donde = {}  # Para almacenar el camino
    g = {inicio: 0}  # Costos g
    f = {inicio: heuristica(inicio, fin)}  # Costos f

    while abierta:
        _, g_actual, actual = heapq.heappop(abierta)
        if actual == fin:
            camino = []
            while actual in de_donde:
                camino.append(actual)
                actual = de_donde[actual]
            return camino[::-1] + [fin]

        usar_dijkstra = heuristica(actual, fin) <= r_dijk
        for dx, dy in direcciones:
            vecino = (actual[0] + dx, actual[1] + dy)
            if es_valida(*vecino, m):
                g_tentativo = g_actual + 1
                f_tentativo = g_tentativo if usar_dijkstra else g_tentativo + heuristica(vecino, fin)
                if vecino not in f or f_tentativo < f.get(vecino, float('inf')):
                    de_donde[vecino] = actual
                    g[vecino] = g_tentativo
                    f[vecino] = f_tentativo
                    heapq.heappush(abierta, (f_tentativo, g_tentativo, vecino))

    return None

# Cargar la matriz desde el archivo YAML
m = cargar_tablero()

# Obtener y mostrar la ruta
ruta = encontrar_camino(m)

print('--------------------------------------------------------------------')
if ruta is None:
    print('=========== xxxxxxxx RUTA NO ENCONTRADA xxxxxxx ============ ')
    print("Camino bloqueado\n")
    for fila in m:
        print(fila)
else:
    print('=========== ¡¡¡¡¡¡¡RUTA ENCONTRADA!!!!! ============ ')
    for paso, (x, y) in enumerate(ruta):
        m[x][y] = 'B'
        print(f"Paso {paso + 1} - Posición: ({x}, {y}):")
        for fila in m:
            print(fila)
        print()
        m[x][y] = '_'
    print("Ruta completa:", ruta)
