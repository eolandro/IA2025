import yaml
import heapq  

# Cargar el tablero desde el archivo YAML
with open('mapa.yaml', 'r') as file:
    data = yaml.safe_load(file)
    mapa = data['Mapa']
    obstruidos = set(data['Obstruidos'])
    inicio = data['Inicial']
    bomba = data['Bomba']

# Crear los nodos y las coordenadas para heurística
nodos = {}
coordenadas = {}
lado = 9  # 9x9

for i in range(len(mapa)):
    nodos[i] = [x for x in mapa[i] if x != i]  # Eliminar referencia a sí mismo
    coordenadas[i] = (i // lado, i % lado)

# Eliminar nodos obstruidos
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

# Imprimir tablero con camino
def imprimir_tablero(paso_actual=None, camino=[]):
    print("\nTablero:")
    for i in range(81):
        if i % 9 == 0 and i != 0:
            print()
        if i == paso_actual:
            print("[*]", end=" ")
        elif i == inicio:
            print("INI", end=" ")
        elif i == bomba:
            print("BMB", end=" ")
        elif i in obstruidos:
            print(" X ", end=" ")
        elif i in camino:
            print(f"[{i:2}]", end=" ")
        else:
            print(f"{i:3}", end=" ")
    print("\n")

# Ejecutar búsqueda
camino = a_estrella(inicio, bomba)

if camino:
    for i in range(len(camino) - 1):
        actual = camino[i]
        siguiente = camino[i + 1]
        imprimir_tablero(actual)
        disponibles = nodos.get(actual, [])
        print(f"Desde {actual} puede moverse a: {disponibles}")
        print(f"Se movió a: {siguiente}\n")

    print("\nTablero final completo:")
    imprimir_tablero(None, camino)

    print("\nRESUMEN FINAL CORRECTO:")
    print("Camino encontrado:", " → ".join(map(str, camino)))
else:
    print("❌ No se encontró un camino.")
