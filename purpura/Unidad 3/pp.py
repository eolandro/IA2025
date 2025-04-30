import yaml

def cargar_arbol(desde_archivo):
    with open(desde_archivo, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def pp(origen, destino):
    arbol = cargar_arbol('arbol.yaml')
    pila = [(origen, [origen])]  
    visitados = set()
    recorrido_completo = []  

    while pila:
        nodo, camino = pila.pop() 
        recorrido_completo.append(nodo)

        if nodo == destino:
            print("Recorrido completo:")
            print(" -> ".join(recorrido_completo))  
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            if nodo in arbol:
                for hijo in reversed(arbol[nodo]):  
                    pila.append((hijo, camino + [hijo]))

    print("No se encontró el destino.")
    return None


while True:
    entrada = input("Usa el formato pa('origen', 'destino')\n")
    print("\n")

    if entrada == 'q':
        print("Saliendo del programa...")
        break

    try:
        if entrada.startswith("pp(") and entrada.endswith(")"):
            eval(entrada)
        else:
            print("Entrada no válida. Usa el formato pp('origen', 'destino').")
    except Exception as e:
        print(f"Error al procesar la entrada: {e}")
    print("presiona q para salir")