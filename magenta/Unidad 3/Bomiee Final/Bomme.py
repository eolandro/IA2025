import heapq
from ruamel.yaml import YAML

yaml = YAML()

# Intentamos cargar el archivo y capturamos errores si el archivo no se encuentra o hay problemas
try:
    with open('tablero.yaml', 'r') as arch:
        datos = yaml.load(arch)
        m = datos['matriz']
except FileNotFoundError:
    print("Error: El archivo 'tablero.yaml' no se encontró.")
    exit()
except KeyError:
    print("Error: El archivo 'tablero.yaml' no contiene la clave 'matriz'.")
    exit()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def es_val(x, y):
    return 0 <= x < len(m) and 0 <= y < len(m[0]) and 'X' not in m[x][y]

def puntos():
    ini = fin = None
    for i, fila in enumerate(m):
        for j, celda in enumerate(fila):
            if 'B' in celda:
                ini = (i, j)
            elif '0' in celda:
                fin = (i, j)
    return ini, fin

def heur(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def camino(r_dijk=5):
    ini, fin = puntos()
    if not ini or not fin:
        return None

    abierta = [(heur(ini, fin), 0, ini)]
    de_donde, g, f = {}, {ini: 0}, {ini: heur(ini, fin)}

    while abierta:
        _, g_act, act = heapq.heappop(abierta)
        if act == fin:
            cam = []
            while act in de_donde:
                cam.append(act)
                act = de_donde[act]
            return cam[::-1] + [fin]

        usar_dijk = heur(act, fin) <= r_dijk
        for dx, dy in dirs:
            vec = (act[0] + dx, act[1] + dy)
            if es_val(*vec):
                g_tent = g_act + 1
                f_tent = g_tent if usar_dijk else g_tent + heur(vec, fin)
                if vec not in f or f_tent < f.get(vec, float('inf')):
                    de_donde[vec] = act
                    g[vec] = g_tent
                    f[vec] = f_tent
                    heapq.heappush(abierta, (f_tent, g_tent, vec))

    return None

ruta = camino()

if ruta is None:
    print('=========== xxxxxxxx RUTA NO ENCONTRADA xxxxxxx ============ ')
    print("Camino bloqueado\n")
    for fila in m:
        print(fila)
else:
    print('=========== ¡¡¡¡¡¡¡RUTA ENCONTRADA!!!!! ============ ')
    for paso, (x, y) in enumerate(ruta):
        m[x][y] = 'B'
        print(f"Paso {paso + 1} - Posición: ({x}, {y}):")
        for fila in m:
            print(fila)
        print()
        m[x][y] = '_'
    print("Ruta completa:", ruta)
