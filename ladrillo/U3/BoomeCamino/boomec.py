import yaml
import time
import os
import heapq  # Para manejar la cola de prioridad de A*

class Boomi:
    def __init__(self, mapa_path):
        self.mapa = self.cargar_mapa(mapa_path)
        self.filas = self.mapa["filas"]
        self.columnas = self.mapa["columnas"]
        self.tablero = self.mapa["tablero"]
        self.posicion = self.encontrar_posicion_inicial()  # Inicializa posición de Boomi desde el mapa
        self.encontrado = False
        self.camino = []  # Ruta óptima hasta el objetivo

    def cargar_mapa(self, mapa_path):
        with open(mapa_path, "r") as file:
            return yaml.safe_load(file)

    def encontrar_posicion_inicial(self):
        for i, fila in enumerate(self.tablero):
            for j, valor in enumerate(fila):
                if valor == "M":
                    self.tablero[i][j] = " "  # Reemplaza "M" por un espacio vacío en el tablero
                    return (i, j)
        return (0, 0)  # Valor por defecto si no encuentra "M"

    def mostrar_tablero(self):
        tablero_con_boomi = [fila[:] for fila in self.tablero]
        for x, y in self.camino:  # Marca el camino en el tablero
            tablero_con_boomi[x][y] = "*"
        x, y = self.posicion
        tablero_con_boomi[x][y] = "A"  # Marca la posición de Boomi con "B"

        os.system("cls" if os.name == "nt" else "clear")
        
        for fila in tablero_con_boomi:
            print(" ".join(fila))
        print("\n")

    def posicion_valida(self, x, y):
        if 0 <= x < self.filas and 0 <= y < self.columnas:
            return self.tablero[x][y] not in ("O", "A")
        return False

    def encontrar_objetivo(self):
        for i, fila in enumerate(self.tablero):
            for j, valor in enumerate(fila):
                if valor == "B":
                    return i, j
        return None

    def heuristica(self, pos, objetivo):
        return abs(pos[0] - objetivo[0]) + abs(pos[1] - objetivo[1])

    def buscar_camino(self):
        print("Buscando el camino hacia el objetivo...")
        for _ in range(5):  # Simula el proceso de búsqueda
            print("Calculando...")
            time.sleep(0.5)

        objetivo = self.encontrar_objetivo()
        if not objetivo:
            print("Objetivo no encontrado en el mapa.")
            return False

        cola = []
        heapq.heappush(cola, (0, self.posicion))
        costos = {self.posicion: 0}
        caminos = {self.posicion: None}

        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while cola:
            _, actual = heapq.heappop(cola)

            if actual == objetivo:
                while actual:
                    self.camino.append(actual)
                    actual = caminos[actual]
                self.camino.reverse()
                return True

            x, y = actual
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy
                if self.posicion_valida(nx, ny):
                    nuevo_costo = costos[actual] + 1
                    if (nx, ny) not in costos or nuevo_costo < costos[(nx, ny)]:
                        costos[(nx, ny)] = nuevo_costo
                        prioridad = nuevo_costo + self.heuristica((nx, ny), objetivo)
                        heapq.heappush(cola, (prioridad, (nx, ny)))
                        caminos[(nx, ny)] = actual

        return False

    def recorrido(self):
        if not self.buscar_camino():
            print("No se encontró un camino hacia el objetivo.")
            return

        print("¡Camino encontrado! Iniciando recorrido...")
        time.sleep(1)

        for paso in self.camino:
            self.posicion = paso
            self.mostrar_tablero()
            time.sleep(0.5)

        print("¡Boomi ha alcanzado el objetivo!")

# Ejecuta la simulación
boomi = Boomi('mapa.yaml')
boomi.recorrido()
