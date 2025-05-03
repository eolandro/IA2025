from ruamel.yaml import YAML

yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

s=open("mapa.yaml","r")
Data = yaml.load(s)
s.close() 
mapa = Data["mapa"]

def buscar_valor(mapa, valor):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == valor:
                return (i,j)

inicio = buscar_valor(mapa, 2)
fin = buscar_valor(mapa, 3)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def obtener_vecinos(nodo, mapa):
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
    vecinos = []
    for i in direcciones:
        x = nodo[0] + i[0]
        y = nodo[1] + i[1]
        if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and mapa[x][y] != 1:
            vecinos.append((x, y))
    return vecinos

def pathfinding(mapa, inicio, fin):
    recorrido = {}
    peso1 = {inicio: 0}
    peso2 = {inicio: manhattan(inicio, fin)}
    calculado = [inicio]

    while calculado:
        actual = min(calculado)

        if actual == fin:
            camino = []
            while actual in recorrido:
                camino.append(actual)
                actual = recorrido[actual]
            camino.append(inicio)
            return list(reversed(camino))

        calculado.remove(actual)

        for vecino in obtener_vecinos(actual, mapa):
            peso_vec = peso1[actual] + 1

            if not vecino in peso1.keys() or peso_vec < peso1[vecino]:
                recorrido[vecino] = actual
                peso1[vecino] = peso_vec
                peso2[vecino] = peso_vec + manhattan(vecino, fin)
                if vecino not in calculado:
                    calculado.append(vecino)

    return None

camino = pathfinding(mapa, inicio, fin)

if camino:
    print("Camino encontrado:")
    for paso in camino:
        print(paso)
else:
    print("No se encontró camino.")