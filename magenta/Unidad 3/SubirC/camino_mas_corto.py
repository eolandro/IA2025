import yaml
import random


def mifuncion(lista):
    if not lista:
        return None
    return random.choice(lista)


with open("grafo.yaml", "r") as file:
    grafo = yaml.safe_load(file)


def camino_mas_corto(grafo, inicio, fin):
    nodos_por_visitar = [(inicio, [inicio], 0)]  
    visitados = set()

    while nodos_por_visitar:
        nodo, camino, costo = nodos_por_visitar.pop(0)

        if nodo == fin:
            return camino, costo

        if nodo in visitados:
            continue

        visitados.add(nodo)

        for vecino in grafo.get(nodo, {}):
            nuevo_costo = costo + grafo[nodo][vecino]
            nodos_por_visitar.append((vecino, camino + [vecino], nuevo_costo))

        
        nodos_por_visitar.sort(key=lambda x: x[2])

    return None, float('inf')  


while True:
    cmd = input("Escribe origen y destino (ej. A I), o 'q' para salir: ")
    if cmd.strip().lower() == 'q':
        break

    try:
        origen, destino = cmd.strip().split()
        if origen not in grafo or destino not in grafo:
            print("Uno de los nodos no existe.")
            continue

        camino, costo = camino_mas_corto(grafo, origen, destino)
        if camino:
            print(f"Camino más corto: {camino} (Costo: {costo})")
            print(f"Random nodo del camino: {mifuncion(camino)}")
        else:
            print("No hay camino disponible.")
    except Exception as e:
        print("Error:", e)
