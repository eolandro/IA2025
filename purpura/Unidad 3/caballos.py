import yaml


def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()

def mover_pieza(tablero, origen, destino):
    tablero[destino[0]][destino[1]] = tablero[origen[0]][origen[1]]
    tablero[origen[0]][origen[1]] = ' '

def cargar_yaml():
    with open('caballos.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

config = cargar_yaml()
tablero = config['tablero_inicial']
movimientos = [(movimiento['origen'], movimiento['destino']) for movimiento in config['movimientos']]

print("Estado inicial:")
imprimir_tablero(tablero)
input("Presiona ENTER para comenzar...\n")

for origen, destino in movimientos:
    mover_pieza(tablero, origen, destino)
    imprimir_tablero(tablero)
    input("Presiona ENTER para mover...\n")

print("Movimiento completado.")
