import random
import yaml
import heapq
from collections import deque

def mifuncion(lista):
    if not lista:
        return None
    return random.choice(lista)

def cargar_grafo_basico():
    with open('grafo.yaml') as f:
        grafo_data = yaml.safe_load(f) or {}
    
    grafo = {}
    for nodo in grafo_data['nodos']:
        grafo[nodo] = []
    
    for arista in grafo_data['aristas']:
        nodo1 = arista['nodo1']
        nodo2 = arista['nodo2']
        grafo[nodo1].append(nodo2)
    
    return grafo

def cargar_grafo_colina():
    with open('grafo_colina.yaml') as f:
        grafo_data = yaml.safe_load(f) or {}
    
    grafo = {}
    for nodo in grafo_data['nodos']:
        grafo[nodo] = []
    
    for arista in grafo_data['aristas']:
        nodo1 = arista['nodo1']
        nodo2 = arista['nodo2']
        peso = arista['peso']
        grafo[nodo1].append((nodo2, peso))
    
    return grafo

def buscar_camino_A(inicio, objetivo):
    grafo = cargar_grafo_basico()
    
    if not all(n in grafo for n in (inicio, objetivo)):
        return f"Error: Nodo(s) no existente(s) en el grafo"
    
    cola = deque([[inicio]])
    visitados = {inicio}
    caminos_explorados = []

    while cola:
        camino = cola.popleft()
        caminos_explorados.append(camino)
        nodo = camino[-1]
        
        if nodo == objetivo:
            return {
                'camino_encontrado': " -> ".join(camino),
                'caminos_explorados': [" -> ".join(p) for p in caminos_explorados]
            }
        
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(camino + [vecino])
    
    return {
        'mensaje': f"No hay camino de {inicio} a {objetivo}",
        'caminos_explorados': [" -> ".join(p) for p in caminos_explorados]
    }

def buscar_camino_P(inicio, objetivo):
    grafo = cargar_grafo_basico()
    
    if not all(n in grafo for n in (inicio, objetivo)):
        return f"Error: Nodo(s) no existente(s) en el grafo"
    
    pila = [[inicio]]
    visitados = set()
    caminos_explorados = []

    while pila:
        camino = pila.pop()
        nodo = camino[-1]
        caminos_explorados.append(camino)
        
        if nodo == objetivo:
            return {
                'camino_encontrado': " -> ".join(camino),
                'caminos_explorados': [" -> ".join(p) for p in caminos_explorados]
            }
        
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in reversed(grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(camino + [vecino])
    
    return {
        'mensaje': f"No hay camino de {inicio} a {objetivo}",
        'caminos_explorados': [" -> ".join(p) for p in caminos_explorados]
    }

def buscar_camino_HC(inicio, objetivo, max_retrocesos=3):
    grafo = cargar_grafo_colina()
    
    if not all(n in grafo for n in (inicio, objetivo)):
        return f"Error: Nodo(s) no existente(s) en el grafo"
    
    # Heurística basada en distancias estimadas al objetivo
    heuristicas = {
        'A': 4, 'B': 5, 'C': 3, 'D': 6, 'E': 4, 
        'F': 5, 'G': 2, 'H': 3, 'I': 1, 'Z': 0
    }
    
    heap = [(0 + heuristicas.get(inicio, 0), 0, inicio, [inicio])]
    visitados = {}
    retrocesos = 0
    
    while heap and retrocesos <= max_retrocesos:
        _, costo_actual, nodo_actual, camino_actual = heapq.heappop(heap)
        
        if nodo_actual == objetivo:
            return {
                'camino_encontrado': " -> ".join(camino_actual),
                'costo_total': costo_actual,
                'mensaje': f"Camino encontrado con Hill Climbing (retrocesos: {retrocesos})"
            }
        
        if nodo_actual in visitados and costo_actual >= visitados[nodo_actual]:
            retrocesos += 1
            continue
        
        visitados[nodo_actual] = costo_actual
        
        for vecino, peso in grafo.get(nodo_actual, []):
            nuevo_costo = costo_actual + peso
            if vecino not in visitados or nuevo_costo < visitados.get(vecino, float('inf')):
                heapq.heappush(
                    heap, 
                    (nuevo_costo + heuristicas.get(vecino, 0), 
                     nuevo_costo, 
                     vecino, 
                     camino_actual + [vecino])
                )
    
    return {
        'mensaje': f"No se encontró camino después de {max_retrocesos} retrocesos",
        'caminos_explorados': []
    }

def mostrar_menu():
    print("\nComandos disponibles:")
    print("1. mifuncion([1,2,3]) - Selección aleatoria")
    print("2. buscar_camino_A('A', 'B') - Búsqueda por anchura (BFS)")
    print("3. buscar_camino_P('A', 'B') - Búsqueda por profundidad (DFS)")
    print("4. buscar_camino_HC('A', 'B') - Hill Climbing con retrocesos")
    print("5. salir (q)")

def mostrar_resultado(resultado):
    if isinstance(resultado, dict):
        if 'caminos_explorados' in resultado and resultado['caminos_explorados']:
            print("\nCaminos explorados:")
            for i, camino in enumerate(resultado['caminos_explorados'], 1):
                print(f"{i}. {camino}")
        
        if 'camino_encontrado' in resultado:
            print("\nCamino encontrado:", resultado['camino_encontrado'])
            if 'costo_total' in resultado:
                print("Costo total:", resultado['costo_total'])
        else:
            print("\nResultado:", resultado['mensaje'])
    else:
        print("\nResultado:", resultado)

def main():
    print("Consola Interactiva de Búsqueda en Grafos")
    print("----------------------------------------")
    print("BFS/DFS usan grafo.yaml")
    print("Hill Climbing usa grafo_colina.yaml")
    
    while True:
        mostrar_menu()
        cmd = input("> ").strip()
        
        if cmd.lower() in ("q", "quit", "exit", "5"):
            break
            
        try:
            resultado = eval(cmd)
            mostrar_resultado(resultado)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()