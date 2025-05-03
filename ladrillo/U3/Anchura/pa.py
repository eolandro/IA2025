import yaml
from collections import deque

G = []

# Función para obtener los hijos de un nodo
def obtener_hijos(G, Raiz):
    return [a for r, a in G if r == Raiz]

# Función para cargar datos del grafo desde un archivo YAML
def cargarDatosYaml():
    global G
    with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/U3/Anchura/gpa.yaml", "r") as file:
        G = yaml.safe_load(file)

# Implementación de búsqueda en primera anchura
def primero_anchura(G, Raiz, Bus):
    # Cola para manejar el recorrido en anchura
    cola = deque([Raiz])
    
    # Conjunto de visitados para evitar ciclos
    visitados = set()
    
    while cola:
        # Tomamos el primer nodo de la cola
        nodo_actual = cola.popleft()
        
        # Imprimimos el nodo actual
        print(f"Visitando nodo: {nodo_actual}")
        
        # Verificamos si es el nodo buscado
        if nodo_actual == Bus:
            print(f"Nodo encontrado: {nodo_actual}")
            return True
        
        # Marcamos el nodo actual como visitado
        visitados.add(nodo_actual)
        
        # Obtenemos los hijos (vecinos) del nodo actual
        hijos = obtener_hijos(G, nodo_actual)
        
        # Añadimos los hijos no visitados a la cola
        for hijo in hijos:
            if hijo not in visitados and hijo not in cola:
                cola.append(hijo)
    
    print(f"Nodo {Bus} no encontrado en el grafo.")
    return False

# Función de consola para interactuar con el programa
def consola():
    Terminar = False
    while not Terminar:
        R = input(">")
        if R == "quit()":
            Terminar = True
            continue
        # Eval permite pasar una cadena como si fuera un código de Python
        try:
            P = eval(R)
            if P:
                print(P)
        except Exception as e:
            print(f"Error: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    cargarDatosYaml()  # Cargar datos al inicio
    consola()