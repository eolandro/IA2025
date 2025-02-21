from analizadorLS   import dLabel
import sys
import pygame

class BoomeVM:
    def __init__(self):         # * Constructor
        pygame.mixer.init()                                                  # @ Pruebas
        self.death = pygame.mixer.Sound('oof.wav')
        
        self.Registros = {
            "AX" : 0, #
            "BX" : 0, #
            "CX" : 0, #
            "DX" : 0, #
        }
        self.Mapa = [
            [3,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,2,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        self.fila, self.columna = 0,0
        self.lineaEjecutando = ""
        self.Vivo = True
        self.etiquetas = {}
    
    def __str__(self):
        tmp =   f"Registros:        {self.Registros}\n"
        tmp +=  f"Linea Ejecutada:  {self.lineaEjecutando}\n"
        tmp +=  f"Vivo:             {self.Vivo}\n"
        tmp +=  f"Posición:         {self.fila},{self.columna}\n\n"
        # tmp +=  f"Etiquetas:        {self.etiquetas}\n\n"
        for l in self.Mapa:
            tmp += str(l) + "\n"
        return tmp
    
    # * Convierte los numeros hex a dec para poder trabajar con ellos
    def convertir(self, N):
        return self.Registros[N] if N in self.Registros else int(N, 16)
    
    def ejecutar_linea(self,linea,indice_actual):        
        self.lineaEjecutando = linea.strip()
        sentencia = linea.split(" ")
        match sentencia:
            case [label]:
                # * Guarda las etiquetas en self.etiquetas
                if dLabel(label):
                    self.etiquetas[label[:-1]] = indice_actual
            case ["mov","r"]:
                self.columna += 1                                       # ! Mover a la derecha
                if self.columna >= len(self.Mapa[self.fila]):
                    self.death.play()
                    self.Vivo = False
                if self.Vivo:
                    if self.Mapa[self.fila][self.columna] in [1, 2]:    # ! Verificar si hay una mina
                        self.death.play()
                        self.Vivo = False
                        self.Mapa[self.fila][self.columna - 1] = 0
                        self.Mapa[self.fila][self.columna] = "D"
                    else:
                        self.Mapa[self.fila][self.columna - 1] = 0
                        self.Mapa[self.fila][self.columna] = 3
            case ["mov","l"]:                                           # ! Mover a la izquierda
                self.columna -= 1
                if self.columna < 0:
                    self.death.play()
                    self.Vivo = False
                if self.Vivo:
                    if self.Mapa[self.fila][self.columna] in [1, 2]:    # ! Verificar si hay una mina
                        self.death.play()
                        self.Vivo = False
                        self.Mapa[self.fila][self.columna + 1] = 0
                        self.Mapa[self.fila][self.columna] = "D"
                    else:
                        self.Mapa[self.fila][self.columna + 1] = 0
                        self.Mapa[self.fila][self.columna] = 3
            case ["mov", "u"]:                                          # ! Mover hacia arriba
                self.fila -= 1
                if self.fila < 0:
                    self.death.play()
                    self.Vivo = False
                if self.Vivo:
                    if self.Mapa[self.fila][self.columna] in [1, 2]:    # ! Verificar si hay una 
                        self.death.play()
                        self.Vivo = False
                        self.Mapa[self.fila + 1][self.columna] = 0
                        self.Mapa[self.fila][self.columna] = "D"
                    else:
                        self.Mapa[self.fila + 1][self.columna] = 0
                        self.Mapa[self.fila][self.columna] = 3
            case ["mov", "d"]:                                          # ! Mover hacia abajo
                self.fila += 1
                if self.fila >= len(self.Mapa):
                    self.death.play()
                    self.Vivo = False
                if self.Vivo:
                    if self.Mapa[self.fila][self.columna] in [1, 2]:    # ! Verificar si hay una mina
                        self.death.play()
                        self.Vivo = False
                        self.Mapa[self.fila - 1][self.columna] = 0
                        self.Mapa[self.fila][self.columna] = "D"
                    else:
                        self.Mapa[self.fila - 1][self.columna] = 0
                        self.Mapa[self.fila][self.columna] = 3
            case ["obs","r"]:
                if self.columna + 1 >= len(self.Mapa[self.fila]): 
                    self.Registros["DX"] = 0x01                         # ! Límite del mapa
                else:
                    if self.Mapa[self.fila][self.columna + 1] == 1:
                        self.Registros["DX"] = 0x01                     # ! Obstáculo detectado
                    else:
                        self.Registros["DX"] = 0
            case ["obs","l"]:
                if self.columna -1 < 0:
                    self.Registros["DX"] = 0x01                         # ! Límite del mapa
                else:
                    if self.Mapa[self.fila][self.columna - 1] == 1:
                        self.Registros["DX"] = 0x01                     # ! Obstáculo detectado
                    else:
                        self.Registros["DX"] = 0
            case ["obs","u"]:
                if self.fila - 1 < 0:
                    self.Registros["DX"] = 0x01                         # ! Límite del mapa
                else:
                    if self.Mapa[self.fila - 1][self.columna] == 1:
                        self.Registros["DX"] = 0x01                     # ! Obstáculo detectado
                    else:
                        self.Registros["DX"] = 0
            case ["obs","d"]:
                if self.fila + 1 >= len(self.Mapa):
                    self.Registros["DX"] = 0x01                         # ! Límite del mapa
                else:
                    if self.Mapa[self.fila + 1][self.columna] == 1:
                        self.Registros["DX"] = 0x01                     # ! Obstáculo detectado
                    else:
                        self.Registros["DX"] = 0
            case ["je",Z1,Z2,Z3]:                                       # ! Salta si son iguales
                n1 = self.convertir(Z1)
                n2 = self.convertir(Z2)
                # print(f"Comparando iguales n1: {n1} con n2: {n2}")
                if n1 == n2 and Z3.rstrip(":") in self.etiquetas:
                    return self.etiquetas[Z3.rstrip(":")]
            case ["jne",Z1,Z2,Z3]:                                      # ! Salta si son diferentes
                n1 = self.convertir(Z1)
                n2 = self.convertir(Z2)
                # print(f"Comparando diferentes n1: {n1} con n2: {n2}")
                if n1 != n2 and Z3.rstrip(":") in self.etiquetas:
                    return self.etiquetas[Z3.rstrip(":")]
            case [Ins,Z1,Z2,Z3]:
                n1 = self.convertir(Z1)
                n2 = self.convertir(Z2)
                
                # * Realiza las operaciones correspondientes
                if Ins == "add":
                    res = n1 + n2
                elif Ins == "sub":
                    res = n1 - n2
                elif Ins == "mul":
                    res = n1 * n2
                elif Ins == "div":
                    if n2 == 0:
                        sys.exit(f"¡Error: División entre cero!")
                    res = n1 // n2
                if res < 0:
                    sys.exit(f"¡Error: No se admiten números negativos!")
                self.Registros[Z3] = res

        return indice_actual + 1