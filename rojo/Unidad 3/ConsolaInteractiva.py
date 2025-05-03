import random
import yaml
import heapq
from collections import deque

def mifuncion(lista):
    if not lista:
        return None
    return random.choice(lista)

def cargar_grafo_basico():
    """Carga el grafo básico sin pesos para BFS/DFS"""
    try:
        with open('grafo.yaml') as f:
            grafo_data = yaml.safe_load(f) or {}
        
        grafo = {nodo: [] for nodo in grafo_data.get('nodos', [])}
        
        for arista in grafo_data.get('aristas', []):
            grafo[arista['nodo1']].append(arista['nodo2'])
        
        return grafo
    except FileNotFoundError:
        print("Error: Archivo grafo.yaml no encontrado")
        return {}

def cargar_grafo_colina():
    """Carga el grafo con pesos para Hill Climbing"""
    try:
        with open('grafo_colina.yaml') as f:
            grafo_data = yaml.safe_load(f) or {}
        
        grafo = {nodo: [] for nodo in grafo_data.get('nodos', [])}
        
        for arista in grafo_data.get('aristas', []):
            grafo[arista['nodo1']].append((arista['nodo2'], arista['peso']))
        
        return grafo
    except FileNotFoundError:
        print("Error: Archivo grafo_colina.yaml no encontrado")
        return {}

def buscar_camino_A(inicio, objetivo):
    """Búsqueda por anchura (BFS)"""
    grafo = cargar_grafo_basico()
    
    if not grafo or not all(n in grafo for n in (inicio, objetivo)):
        return {'mensaje': "Error: Nodo(s) no existente(s) en el grafo"}
    
    cola = deque([[inicio]])
    visitados = {inicio}
    caminos_explorados = []

    while cola:
        camino = cola.popleft()
        caminos_explorados.append(camino)
        nodo = camino[-1]
        
        if nodo == objetivo:
            return {
                'camino_encontrado': " → ".join(camino),
                'caminos_explorados': [" → ".join(p) for p in caminos_explorados],
                'longitud': len(camino)-1
            }
        
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(camino + [vecino])
    
    return {
        'mensaje': f"No hay camino de {inicio} a {objetivo}",
        'caminos_explorados': [" → ".join(p) for p in caminos_explorados]
    }

def buscar_camino_P(inicio, objetivo):
    """Búsqueda por profundidad (DFS)"""
    grafo = cargar_grafo_basico()
    
    if not grafo or not all(n in grafo for n in (inicio, objetivo)):
        return {'mensaje': "Error: Nodo(s) no existente(s) en el grafo"}
    
    pila = [[inicio]]
    visitados = set()
    caminos_explorados = []

    while pila:
        camino = pila.pop()
        nodo = camino[-1]
        caminos_explorados.append(camino)
        
        if nodo == objetivo:
            return {
                'camino_encontrado': " → ".join(camino),
                'caminos_explorados': [" → ".join(p) for p in caminos_explorados],
                'longitud': len(camino)-1
            }
        
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in reversed(grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(camino + [vecino])
    
    return {
        'mensaje': f"No hay camino de {inicio} a {objetivo}",
        'caminos_explorados': [" → ".join(p) for p in caminos_explorados]
    }

def buscar_camino_HC(inicio, objetivo, max_retrocesos=10):
    """Hill Climbing con heurística mejorada"""
    grafo = cargar_grafo_colina()
    
    if not grafo or not all(n in grafo for n in (inicio, objetivo)):
        return {'mensaje': "Error: Nodo(s) no existente(s) en el grafo"}
    
    # Heurística optimizada para el grafo_colina.yaml
    heuristicas = {
        'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 
        'F': 2, 'G': 1, 'H': 1, 'I': 0, 'Z': 5
    }
    
    heap = [(heuristicas.get(inicio, 0), 0, inicio, [inicio])]  # (heurística + costo, costo, nodo, camino)
    visitados = {}
    retrocesos = 0
    
    while heap and retrocesos <= max_retrocesos:
        _, costo_actual, nodo_actual, camino_actual = heapq.heappop(heap)
        
        if nodo_actual == objetivo:
            return {
                'camino_encontrado': " → ".join(camino_actual),
                'costo_total': costo_actual,
                'longitud': len(camino_actual)-1,
                'retrocesos': retrocesos,
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
        'retrocesos': retrocesos,
        'caminos_explorados': []
    }

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n╔═════════════════════════════════╗")
    print("║      CONSOLA DE BÚSQUEDA        ║")
    print("╠═════════════════════════════════╣")
    print("║ 1. mifuncion([1,2,3])           ║")
    print("║ 2. buscar_camino_A('A', 'B')    ║")
    print("║ 3. buscar_camino_P('A', 'B')    ║")
    print("║ 4. buscar_camino_HC('A', 'B')   ║")
    print("║ 5. salir (q)                    ║")
    print("╚═════════════════════════════════╝")

def mostrar_resultado(resultado):
    """Muestra los resultados de forma organizada"""
    if isinstance(resultado, dict):
        if 'camino_encontrado' in resultado:
            print("═"*40)
            print(f" CAMINO ENCONTRADO: {resultado['camino_encontrado']}")
            if 'costo_total' in resultado:
                print(f" Costo total: {resultado['costo_total']}")
            if 'longitud' in resultado:
                print(f" Longitud: {resultado['longitud']} pasos")
            if 'retrocesos' in resultado:
                print(f" Retrocesos: {resultado['retrocesos']}")
            print("═"*40)
        
        if 'caminos_explorados' in resultado and resultado['caminos_explorados']:
            print("\nÚltimos 5 caminos explorados:")
            for i, camino in enumerate(resultado['caminos_explorados'][-5:], 1):
                print(f" {i}. {camino}")
        
        if 'mensaje' in resultado:
            print(f"\n{resultado['mensaje']}")
    else:
        print("\nResultado:", resultado)

def main():
    
    while True:
        mostrar_menu()
        cmd = input("\n>> ").strip()
        print("\n")
        
        if cmd.lower() in ("q", "quit", "exit", "5"):
            break
            
        try:
            resultado = eval(cmd)
            mostrar_resultado(resultado)
        except Exception as e:
            print(f"\nError: {e}\nPor favor ingrese un comando válido.")

if __name__ == "__main__":
    main()