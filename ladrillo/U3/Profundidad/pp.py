G = []

# Función para obtener los hijos de un nodo
def obtener_hijos(G, Raiz):
    return [a for r, a in G if r == Raiz]

# Función para cargar datos del grafo
def cargarDatos():
    import json
    with open("gpp.yaml") as entrada:
        R = json.load(entrada)
        G.extend(R)

# Implementación de búsqueda en profundidad pura (sin bucles)
def primero_profundidad(G, Raiz, Bus, visitados=None, camino=None):
    if visitados is None:
        visitados = set()  # Para llevar un registro de los nodos ya visitados
    if camino is None:
        camino = []  # Para llevar un registro del camino recorrido

    # Agregar el nodo actual al camino
    camino.append(Raiz)
    print(f"Visitando nodo: {Raiz}")

    # Verificar si hemos encontrado el nodo de destino
    if Raiz == Bus:
        print(f"Nodo encontrado: {Raiz}")
        return True

    # Marcar el nodo como visitado
    visitados.add(Raiz)

    # Obtener los hijos del nodo actual
    hijos = obtener_hijos(G, Raiz)

    # Función recursiva para visitar los hijos
    def visitar_hijos(hijos):
        if not hijos:  # Si no hay más hijos, retornar False
            camino.pop()  # Retroceder en el camino
            return False
        hijo = hijos[0]  # Tomar el primer hijo
        if hijo not in visitados:  # Si no ha sido visitado
            if primero_profundidad(G, hijo, Bus, visitados, camino):
                return True
        return visitar_hijos(hijos[1:])  # Visitar el resto de los hijos

    return visitar_hijos(hijos)  # Iniciar la visita a los hijos

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
    cargarDatos()  # Cargar datos al inicio
    consola()