import numpy as np
import yaml

class NeutralizaBombas:
    def __init__(self, ancho=10, largo=5):
        self.ancho = ancho
        self.largo = largo
        self.ubicacion_actual = [0, 0]
        self.intentos_disponibles = 3
        self.bombas_neutralizadas = 0
        self.posiciones_visitadas = set()
        self.sentido_desplazamiento = 1
        self.zona = self.generar_zona()

    def generar_zona(self):
        zona = [['0' for _ in range(self.ancho)] for _ in range(self.largo)]
        zona[1][2] = '💣'  
        return zona

    def mostrar_zona(self):
        print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("\nZona Actal:")
        zona_str = '\n'.join([' '.join(fila) for fila in self.zona])
        print(zona_str)
        print(f"Intentos disponibles: {self.intentos_disponibles}\n")

    def refrescar_zona(self):
        for fila in range(self.largo):
            for col in range(self.ancho):
                if self.zona[fila][col] == '🤖':
                    self.zona[fila][col] = '0'

        fila_act, col_act = self.ubicacion_actual
        if self.zona[fila_act][col_act] != '💣':
            self.zona[fila_act][col_act] = '🤖'

    def desplazar(self):
        nueva_columna = self.ubicacion_actual[1] + self.sentido_desplazamiento
        if 0 <= nueva_columna < self.ancho:
            self.ubicacion_actual[1] = nueva_columna
        elif self.ubicacion_actual[0] < self.largo - 1:
            self.ubicacion_actual[0] += 1
            self.sentido_desplazamiento *= -1

    def calcular_probabilidad_bayesiana(self, fila, columna, posiciones_restantes):
        probabilidad_bayes = 0
        estimaciones = []

        for intento in range(2):
            prob = np.random.rand()
            print(f"Probabilidad generada para intento {intento+1}: {prob:.4f}")
            if self.zona[fila][columna] == "🤖":
                estimaciones.append(1 if prob > 0.90 else 0)
            else:
                estimaciones.append(1 if prob <= 1.0 else 0)

        prob = np.random.rand()
        print(f"Probabilidad de Bayes: {prob:.4f}")
        if self.zona[fila][columna] == "🤖":
            estimaciones.append(1 if prob > 0.90 else 0)
        else:
            estimaciones.append(1 if prob <= 1.0 else 0)

        if estimaciones.count(1) > 0:
            for uno in range(estimaciones.count(1)):
                if uno == 0:
                    if posiciones_restantes > 0:
                        probabilidad_bayes = (0.9 * (1 / posiciones_restantes)) / (
                            (1 / posiciones_restantes) * 0.9 + (1 - (1 / posiciones_restantes)) * 0.2
                        )
                else:
                    probabilidad_bayes = (0.9 * probabilidad_bayes) / (
                        probabilidad_bayes * 0.9 + (1 - probabilidad_bayes) * 0.2
                    )

        probabilidad_final = max(probabilidad_bayes, 0.01)
        return probabilidad_final >= 0.31

    def guardar_zona(self):
        with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/U2/Boome/zbomba.yaml", "w", encoding="utf-8") as archivo:
            yaml.dump(self.zona, archivo, allow_unicode=True)

    def cargar_zona(self):
        with open("C:/Users/ramir/Downloads/Ultimo Semestre/IA/U2/Boome/zbomba.yaml", "r", encoding="utf-8") as archivo:
            self.zona = yaml.safe_load(archivo)
        print("Mapa de bombas cargado desde zona_bombas.yaml")

    def iniciar_partida(self):
        total_posiciones = self.ancho * self.largo

        for _ in range(total_posiciones):
            self.refrescar_zona()
            self.mostrar_zona()

            posicion_actual = tuple(self.ubicacion_actual)
            self.posiciones_visitadas.add(posicion_actual)
            posiciones_restantes = self.ancho * self.largo - len(self.posiciones_visitadas)

            probabilidad_bomba = self.calcular_probabilidad_bayesiana(
                self.ubicacion_actual[0],
                self.ubicacion_actual[1],
                posiciones_restantes
            )

            if self.intentos_disponibles > 0:
                if probabilidad_bomba:
                    print("!!BOMBA NEUTRALIZADA!!", end=' - ')
                    if self.zona[self.ubicacion_actual[0]][self.ubicacion_actual[1]] == '💣':
                        self.bombas_neutralizadas += 1
                    else:
                        print("!FALSA ALARMA, NO HAY BOMBA!")
                    self.intentos_disponibles -= 1
            else:
                print("Sin intentos disponibles para neutralizar bombas.")
                break

            self.desplazar()

        print(f"Bombas neutralizadas: {self.bombas_neutralizadas}")

partida = NeutralizaBombas()
partida.guardar_zona()  
partida.cargar_zona()   
partida.iniciar_partida()  
