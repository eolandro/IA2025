from ruamel.yaml import YAML
from copy import deepcopy

yaml_parser = YAML()
yaml_parser.indent(sequence=4, offset=2)
yaml_parser.default_flow_style = False

def cargar_configuracion(archivo):
    with open(archivo) as f:
        return yaml_parser.load(f)["grid"]

def localizar_celda(tablero, objetivo):
    for idx, fila in enumerate(tablero):
        if objetivo in fila:
            return (idx, fila.index(objetivo))
    return None

def calcular_heuristica(punto_a, punto_b):
    return abs(punto_a[0] - punto_b[0]) + abs(punto_a[1] - punto_b[1])

def explorar_adyacentes(posicion_actual, tablero):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    celdas_validas = []
    
    for dx, dy in movimientos:
        nx, ny = posicion_actual[0] + dx, posicion_actual[1] + dy
        if 0 <= nx < len(tablero) and 0 <= ny < len(tablero[0]):
            if tablero[nx][ny] != 1:
                celdas_validas.append((nx, ny))
    return celdas_validas

def buscar_ruta(tablero, origen, destino):
    rutas_registradas = {}
    coste_real = {origen: 0}
    coste_estimado = {origen: calcular_heuristica(origen, destino)}
    nodos_abiertos = [origen]

    while nodos_abiertos:
        nodo_actual = min(nodos_abiertos, key=lambda x: coste_estimado[x])

        if nodo_actual == destino:
            trayectoria = []
            while nodo_actual in rutas_registradas:
                trayectoria.append(nodo_actual)
                nodo_actual = rutas_registradas[nodo_actual]
            trayectoria.append(origen)
            return trayectoria[::-1]

        nodos_abiertos.remove(nodo_actual)

        for vecino in explorar_adyacentes(nodo_actual, tablero):
            nuevo_cost = coste_real[nodo_actual] + 1

            if vecino not in coste_real or nuevo_cost < coste_real[vecino]:
                rutas_registradas[vecino] = nodo_actual
                coste_real[vecino] = nuevo_cost
                coste_estimado[vecino] = nuevo_cost + calcular_heuristica(vecino, destino)
                if vecino not in nodos_abiertos:
                    nodos_abiertos.append(vecino)

    return None

def dibujar_tablero(tablero, trayectoria=None):
    simbolos = {
        0: ' ',
        1: '#',
        2: 'S',
        3: 'E',
        4: '*'
    }
    
    if trayectoria:
        tablero_visual = deepcopy(tablero)
        for paso in trayectoria[1:-1]:
            x, y = paso
            tablero_visual[x][y] = 4
    else:
        tablero_visual = tablero
    
    ancho = len(tablero_visual[0])
    borde = '+' + ('---+' * ancho)
    
    print(borde)
    for fila in tablero_visual:
        fila_str = '| ' + ' | '.join(simbolos[celda] for celda in fila) + ' |'
        print(fila_str)
        print(borde)

# Ejecución principal
cuadricula = cargar_configuracion("grid.yaml")

print("\n=== MAPA ORIGINAL ===")
dibujar_tablero(cuadricula)
print("\nLeyenda:")
print("S: Inicio | E: Fin | #: Obstáculo | Espacio: Celda vacía")

punto_inicio = localizar_celda(cuadricula, 2)
punto_final = localizar_celda(cuadricula, 3)

if punto_inicio and punto_final:
    ruta_optima = buscar_ruta(cuadricula, punto_inicio, punto_final)
    
    if ruta_optima:
        print("\n=== RUTA ENCONTRADA ===")
        dibujar_tablero(cuadricula, ruta_optima)
        print("\nLeyenda actualizada:")
        print("*: Camino | S: Inicio | E: Fin | #: Obstáculo")
        print("\nCoordenadas del camino:")
        for coord in ruta_optima:
            print(f"({coord[0]}, {coord[1]})")
    else:
        print("\nNo existe camino válido entre los puntos")
else:
    print("\nError: Puntos de inicio/fin no encontrados")
