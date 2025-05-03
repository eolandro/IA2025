import yaml
import os

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

# Crear el nodo raíz
raiz = Nodo("Z")

# Crear los nodos hijos directos de Z
nodo_ZZ = Nodo("ZZ")
nodo_ZY = Nodo("ZY")
nodo_ZX = Nodo("ZX")
nodo_ZW = Nodo("ZW")

raiz.hijos = [nodo_ZZ, nodo_ZY, nodo_ZX, nodo_ZW]

# Hijos de ZZ
nodo_ZZZ = Nodo("ZZZ")
nodo_ZZY = Nodo("ZZY")
nodo_ZZYZ = Nodo("ZZYZ")
nodo_ZZY.hijos = [nodo_ZZYZ]
nodo_ZZ.hijos = [nodo_ZZZ, nodo_ZZY]

# Hijos de ZY
nodo_ZYZ = Nodo("ZYZ")
nodo_ZYY = Nodo("ZYY")
nodo_ZY.hijos = [nodo_ZYZ, nodo_ZYY]

# Hijos de ZX
nodo_ZXZ = Nodo("ZXZ")
nodo_ZXY = Nodo("ZXY")
nodo_ZXZZ = Nodo("ZXZZ")
nodo_ZXZ.hijos = [nodo_ZXZZ]
nodo_ZX.hijos = [nodo_ZXZ, nodo_ZXY]

# Hijos de ZW
nodo_ZWZ = Nodo("ZWZ")
nodo_ZWY = Nodo("ZWY")
nodo_ZWYZ = Nodo("ZWYZ")
nodo_ZWZ.hijos = [nodo_ZWYZ]
nodo_ZW.hijos = [nodo_ZWZ, nodo_ZWY]

# Función para convertir árbol a diccionario
def arbol_a_diccionario(nodo):
    return {nodo.valor: [arbol_a_diccionario(hijo) for hijo in nodo.hijos]}

# Ruta donde guardar el archivo YAML
ruta_archivo = "c:/Users/Acer/Documents/IA/arbol.yaml"
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

# Guardar en YAML
with open(ruta_archivo, "w") as f:
    yaml.dump(arbol_a_diccionario(raiz), f, sort_keys=False)
