import yaml
import heapq #Para manejar una cola de prioridad usada en el algoritmo A*.

# Cargar el tablero desde el archivo YAML
with open('mapa.yaml', 'r') as file:
    data = yaml.safe_load(file)
    tablero = data['tablero']

# Parámetros del problema
obstruidos = {12, 30, 59} # Son las celdas en donde se encuentran los obstaculos
inicio = 10               # Es el inicio y esta representada en el tablero como INI
bomba = 60                # Es el objetivo y esta representada en el tablero como BMB

#Contamos las filas y columnas que tiene el tablero 
filas = len(tablero)
columnas = len(tablero[0])

# Se crean las coordenadas y los nodos vecinos
coordenadas = {}
nodos = {}

for i in range(filas):
    for j in range(columnas):
        val = tablero[i][j]
        coordenadas[val] = (i, j)
        vecinos = []
        if i > 0: vecinos.append(tablero[i-1][j])              # Arriba
        if i < filas - 1: vecinos.append(tablero[i+1][j])      # Abajo
        if j > 0: vecinos.append(tablero[i][j-1])              # Izquierda
        if j < columnas - 1: vecinos.append(tablero[i][j+1])   # Derecha
        nodos[val] = vecinos

# Aquí se eliminan los nodos obstruidos 
for obs in obstruidos:
    if obs in nodos:
        for vecino in nodos[obs]:
            if vecino in nodos and obs in nodos[vecino]:
                nodos[vecino].remove(obs)
        del nodos[obs]

# Heurística Manhattan
def heuristica(a, b):
    ax, ay = coordenadas[a]
    bx, by = coordenadas[b]
    return abs(ax - bx) + abs(ay - by)

# A*
def a_estrella(inicio, objetivo):
    cola = []
    heapq.heappush(cola, (0, inicio))
    caminos = {inicio: None}
    costos = {inicio: 0}

    while cola:
        _, actual = heapq.heappop(cola)

        if actual == objetivo:
            ruta = []
            while actual is not None:
                ruta.append(actual)
                actual = caminos[actual]
            ruta.reverse()
            return ruta

        for vecino in nodos.get(actual, []):
            nuevo_costo = costos[actual] + 1
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, objetivo)
                heapq.heappush(cola, (prioridad, vecino))
                caminos[vecino] = actual

    return None

# Salida Tablero
def imprimir_tablero(paso_actual=None, camino=[]):
    print("\nTablero:")
    for i in range(filas):
        for j in range(columnas):
            val = tablero[i][j]
            if val == paso_actual:
                print("[*]", end=" ")
            elif val == inicio:
                print("INI", end=" ")
            elif val == bomba:
                print("BMB", end=" ")
            elif val in obstruidos:
                print(" X ", end=" ")
            elif val in camino:
                print(f"[{val}]", end=" ")
            else:
                print(f"{val:3}", end=" ")
        print()

# Ejecutar
camino = a_estrella(inicio, bomba)

if camino:
    for i in range(len(camino) - 1):
        actual = camino[i]
        siguiente = camino[i + 1]
        imprimir_tablero(actual)
        disponibles = nodos.get(actual, [])
        print(f"Desde {actual} puede moverse a: {disponibles}")
        print(f"Se movió a: {siguiente}\n")

    # Tablero final
    print("\nTablero final completo:")
    imprimir_tablero(None, camino)

    print("\nRESUMEN FINAL CORRECTO:")
    print("Camino encontrado:", " → ".join(map(str, camino)))
else:
    print("❌ No se encontró un camino.")
