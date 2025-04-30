import yaml
import heapq

def cargar_grafo(archivo_yaml):
    """Carga el grafo desde un archivo YAML"""
    with open(archivo_yaml, 'r') as file:
        grafo_data = yaml.safe_load(file)
    
    grafo = {}
    for nodo in grafo_data['nodos']:
        grafo[nodo] = []
    
    for arista in grafo_data['aristas']:
        nodo1 = arista['nodo1']
        nodo2 = arista['nodo2']
        peso = arista['peso']
        grafo[nodo1].append((nodo2, peso))
    
    return grafo

def dijkstra_con_retrocesos(grafo, inicio, objetivo, max_retrocesos=4):
    """Implementa el algoritmo de Dijkstra con máximo retrocesos permitidos"""
    heap = [(0, inicio, [inicio])]
    visitados = {}
    retrocesos = 0
    
    while heap and retrocesos <= max_retrocesos:
        costo_actual, nodo_actual, camino_actual = heapq.heappop(heap)
        
        if nodo_actual == objetivo:
            return (camino_actual, costo_actual)
        
        if nodo_actual in visitados and costo_actual >= visitados[nodo_actual]:
            retrocesos += 1
            continue
        
        visitados[nodo_actual] = costo_actual
        
        for vecino, peso in grafo.get(nodo_actual, []):
            if vecino not in visitados or costo_actual + peso < visitados.get(vecino, float('inf')):
                heapq.heappush(heap, (costo_actual + peso, vecino, camino_actual + [vecino]))
    
    return (None, float('inf'))

def main():
    # Cargar el grafo
    grafo = cargar_grafo('grafo_colina.yaml')
    
    # Mostrar nodos disponibles y solicitar entrada
    print("Nodos disponibles:", list(grafo.keys()))
    inicio = input("Ingrese el nodo inicial => ").upper()
    objetivo = input("Ingrese el nodo objetivo => ").upper()
    
    # Validar entradas
    if inicio not in grafo or objetivo not in grafo:
        print("Error: Nodo inicial o objetivo no válido")
        return
    
    # Ejecutar Dijkstra con retrocesos
    camino, costo = dijkstra_con_retrocesos(grafo, inicio, objetivo, max_retrocesos=4)
    
    # Mostrar resultados
    print("\nResultados:")
    if camino:
        print(f"Camino encontrado => {' -> '.join(camino)}")
        print(f"Costo total: {costo}")
    else:
        print("No se encontró un camino válido después de 4 retrocesos.")

if __name__ == "__main__":
    main()
