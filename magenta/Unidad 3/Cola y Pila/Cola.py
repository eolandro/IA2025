import yaml
from collections import deque
import random

# Clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

# Convertir diccionario a árbol de Nodo
def diccionario_a_arbol(dic):
    for clave, lista in dic.items():
        nodo = Nodo(clave)
        for hijo_dic in lista:
            hijo_nodo = diccionario_a_arbol(hijo_dic)
            nodo.hijos.append(hijo_nodo)
        return nodo

# Buscar nodo por valor
def encontrar_nodo(nodo, valor_buscado):
    if nodo.valor == valor_buscado:
        return nodo
    for hijo in nodo.hijos:
        resultado = encontrar_nodo(hijo, valor_buscado)
        if resultado:
            return resultado
    return None

# Buscar ruta desde origen hasta destino con recorrido completo
def buscar_ruta(origen, destino_valor):
    recorrido = []
    rutas_encontradas = []

    cola = deque([(origen, [origen.valor])])
    while cola:
        nodo, camino = cola.popleft()
        recorrido.append(nodo.valor)

        for hijo in nodo.hijos:
            nuevo_camino = camino + [hijo.valor]
            cola.append((hijo, nuevo_camino))

            if hijo.valor == destino_valor:
                rutas_encontradas.append(nuevo_camino)

    # Mostrar recorrido completo
    print("\nRecorrido completo:")
    print(" -> ".join(recorrido))

    # Mostrar rutas
    if rutas_encontradas:
        print("\nRuta(s) al destino:")
        for ruta in rutas_encontradas:
            print(" -> ".join(ruta))
    else:
        print("\nNo se encontró una ruta al destino.")

    return ""  # Para que el REPL no imprima 'None'

# Cargar árbol desde archivo YAML
ruta_archivo = "c:/Users/Acer/Documents/IA/arbol.yaml"
with open(ruta_archivo, "r") as f:
    diccionario = yaml.safe_load(f)
    raiz = diccionario_a_arbol(diccionario)

# Función que evalúa el usuario
def PC(origen_valor, destino_valor):
    origen_nodo = encontrar_nodo(raiz, origen_valor)
    if not origen_nodo:
        print(f"No se encontró el nodo de origen: {origen_valor}")
        return ""
    return buscar_ruta(origen_nodo, destino_valor)

# Función auxiliar (no modificada)
def mifuncion(lista):
    if not lista:
        return None
    return random.choice(lista)

# REPL
print("Escribe PC(\"origen\", \"destino\") para buscar. Escribe 'q' para salir.")
while True:
    cmd = input(">")
    if cmd == 'q':
        break
    try:
        R = eval(cmd)
        if R is not None:
            print(R)
    except Exception as e:
        print("Error en la entrada. Asegúrate de escribir: PC(\"origen\", \"destino\")")
