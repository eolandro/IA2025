import random
import yaml
from collections import deque

# Función original
def mifuncion(lista):
    if not lista:
        return None
    return random.choice(lista)

def cargar_grafo():
    """Carga el grafo desde el archivo YAML"""
    with open('grafo.yaml') as f:
        return yaml.safe_load(f) or {}

# Función de búsqueda por anchura (BFS)
def buscar_camino_A(inicio, objetivo):
    grafo = cargar_grafo()
    
    # Verificar que los nodos existan
    if not all(n in grafo for n in (inicio, objetivo)):
        return f"Error: Nodo(s) no existente(s) en el grafo"
    
    # Algoritmo de búsqueda por amplitud
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

# Función de búsqueda en profundidad (DFS)
def buscar_camino_P(inicio, objetivo):
    grafo = cargar_grafo()
    
    # Verificar que los nodos existan
    if not all(n in grafo for n in (inicio, objetivo)):
        return f"Error: Nodo(s) no existente(s) en el grafo"
    
    # Algoritmo de búsqueda en profundidad
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
            # Añadimos los vecinos en orden inverso para explorar de izquierda a derecha
            for vecino in reversed(grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(camino + [vecino])
    
    return {
        'mensaje': f"No hay camino de {inicio} a {objetivo}",
        'caminos_explorados': [" -> ".join(p) for p in caminos_explorados]
    }

# REPL interactivo - Consola Interactiva
def mostrar_menu():
    print("\nComandos disponibles:")
    print("1. mifuncion([1,2,3]) - Selección aleatoria")
    print("2. buscar_camino_A('A', 'B') - Búsqueda por anchura (BFS)")
    print("3. buscar_camino_P('A', 'B') - Búsqueda por profundidad (DFS)")
    print("4. salir (q)")

def mostrar_resultado(resultado):
    if isinstance(resultado, dict):
        print("\nCaminos explorados:")
        for i, camino in enumerate(resultado['caminos_explorados'], 1):
            print(f"{i}. {camino}")
        
        if 'camino_encontrado' in resultado:
            print("\nCamino encontrado:", resultado['camino_encontrado'])
        else:
            print("\nResultado:", resultado['mensaje'])
    else:
        print("\nResultado:", resultado)

def main():
    while True:
        mostrar_menu()
        cmd = input("> ").strip()
        
        if cmd.lower() == "q":
            break
            
        try:
            resultado = eval(cmd)
            mostrar_resultado(resultado)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()