import yaml

def cargar_arbol(desde_archivo):
    with open(desde_archivo, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def pa(origen, destino):
    arbol = cargar_arbol('arbol.yaml')
    cola = [(origen, [origen])]
    visitados = set()
    recorrido_completo = []  

    while cola:
        nodo, camino = cola.pop(0)
        recorrido_completo.append(nodo)  

        if nodo == destino:
            print("Recorrido completo:")
            print(" -> ".join(recorrido_completo))  
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            if nodo in arbol:
                for hijo in arbol[nodo]:
                    cola.append((hijo, camino + [hijo]))

    print("No se encontró el destino.")
    return None


while True:
    print("\n")
    entrada = input("Usa el formato pa('origen', 'destino')\n")
    print("presiona q para salir")
    if entrada == 'q':
        print("Saliendo del programa...")
        break
    try:
        if entrada.startswith("pa(") and entrada.endswith(")"):
            eval(entrada)
        else:
            print("Entrada no válida. Usa el formato pa('origen', 'destino').")
    except Exception as e:
        print(f"Error al procesar la entrada: {e}")
    print("presiona q para salir")
