import yaml

def cargar_mapa(nombre_archivo):
    with open(nombre_archivo, 'r',encoding='utf-8') as archivo:
        datos = yaml.safe_load(archivo)
    return datos['Map']

def buscar_posiciones(mapa):
    inicio = meta = None
    for i, fila in enumerate(mapa):
        for j, valor in enumerate(fila):
            if valor == 'R':
                inicio = (i, j)
            elif valor == 'B':
                meta = (i, j)
    if inicio is None:
        print("No se encontró la meta ('R') en el mapa.")
    if meta is None:
        print("No se encontró a Boome ('B') en el mapa.")

    return inicio, meta

def calculo_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def busqueda_camino(mapa, inicio, meta):
    disponible = [(0, inicio)]
    posicion = {inicio: None}
    costos = {inicio: 0}
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pared = '█'
    mapa_explorado = [fila[:] for fila in mapa]

    while disponible:
        bajo_costo = 0
        for i in range(1, len(disponible)):
            if disponible[i][0] < disponible[bajo_costo][0]:
                bajo_costo = i
        _, actual = disponible.pop(bajo_costo)

        if mapa_explorado[actual[0]][actual[1]] == ' ':
            mapa_explorado[actual[0]][actual[1]] = 'x'

        if actual == meta:
            break

        for mover in movimientos:
            vecino = (actual[0] + mover[0], actual[1] + mover[1])

            if (0 <= vecino[0] < len(mapa) and 0 <= vecino[1] < len(mapa[0]) 
                and mapa[vecino[0]][vecino[1]] != pared):
                costo2 = costos[actual] + 1

                if vecino not in costos or costo2 < costos[vecino]:
                    costos[vecino] = costo2
                    prioridad = costo2 + calculo_dis(meta, vecino)
                    disponible.append((prioridad, vecino))
                    posicion[vecino] = actual

    return marcar_caminito(posicion, inicio, meta), mapa_explorado

def marcar_caminito(posicion, inicio, meta):
    camino = []
    actual = meta
    while actual != inicio:
        camino.append(actual)
        actual = posicion.get(actual)
        if actual is None:
            return None
    camino.append(inicio)
    camino.reverse()
    return camino

def mostrar_mapa(mapa, mensaje="Mapa"):
    print(f"\n{mensaje}:")
    for fila in mapa:
        print(" ".join(fila))

def marcar_camino(mapa, camino, simbolo="•"):
    for x, y in camino:
        if mapa[x][y] == ' ':
            mapa[x][y] = simbolo

mapa = cargar_mapa('camino.yaml')
inicio, meta = buscar_posiciones(mapa)

if inicio is None or meta is None:
    print("No se puede continuar sin Boome o sin la meta.")
    exit()

mostrar_mapa(mapa, "Mapa inicial")
camino, mapa_explorado = busqueda_camino(mapa, inicio, meta)

if camino:
    mostrar_mapa(mapa_explorado, "Recorrido de boome")
    camino_final = [fila[:] for fila in mapa]
    marcar_camino(camino_final, camino, simbolo="•")
    mostrar_mapa(camino_final, "Camino final")
else:
    print("No se encontró un camino.")
