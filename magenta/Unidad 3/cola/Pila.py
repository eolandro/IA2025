import yaml
import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def diccionario_a_arbol(dic):
    for clave, lista in dic.items():
        nodo = Nodo(clave)
        for hijo_dic in lista:
            hijo_nodo = diccionario_a_arbol(hijo_dic)
            nodo.hijos.append(hijo_nodo)
        return nodo

def encontrar_nodo(nodo, valor_buscado):
    if nodo.valor == valor_buscado:
        return nodo
    for hijo in nodo.hijos:
        resultado = encontrar_nodo(hijo, valor_buscado)
        if resultado:
            return resultado
    return None

def buscar_ruta_profundidad(origen, destino_valor):
    recorrido = []
    rutas_encontradas = []

    pila = [(origen, [origen.valor])]
    while pila:
        nodo, camino = pila.pop()
        recorrido.append(nodo.valor)

        for hijo in reversed(nodo.hijos):
            nuevo_camino = camino + [hijo.valor]
            pila.append((hijo, nuevo_camino))
            if hijo.valor == destino_valor:
                rutas_encontradas.append(nuevo_camino)

    print("\nRecorrido completo:")
    print(" -> ".join(recorrido))

    if rutas_encontradas:
        print("\nRuta(s) al destino:")
        for ruta in rutas_encontradas:
            print(" -> ".join(ruta))
    else:
        print("\nNo se encontró una ruta al destino.")

    return ""

ruta_archivo = "c:/Users/Acer/Documents/IA/arbol.yaml"
with open(ruta_archivo, "r") as f:
    diccionario = yaml.safe_load(f)
    raiz = diccionario_a_arbol(diccionario)

def PP(origen_valor, destino_valor):
    origen_nodo = encontrar_nodo(raiz, origen_valor)
    if not origen_nodo:
        print(f"No se encontró el nodo de origen: {origen_valor}")
        return ""
    return buscar_ruta_profundidad(origen_nodo, destino_valor)

def mifuncion(lista):
    if not lista:
        return None
    return random.choice(lista)

print("Escribe PP(\"origen\", \"destino\") para buscar. Escribe 'q' para salir.")
while True:
    cmd = input(">")
    if cmd == 'q':
        break
    try:
        R = eval(cmd)
        if R is not None:
            print(R)
    except Exception:
        print("Error en la entrada. Asegúrate de escribir: PP(\"origen\", \"destino\")")
