class BoomieVM():
    def __init__(self):
        self.Registros = {
            "AX": 0,
            "BX": 0,
            "CX": 0,
            "DX": 0 #obs overwrites this
        }

        self.Mapa=[
            [3,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,2,0,0],
            [0,0,0,0,0,0,0,2]
        ]
        self.fila, self.columna = 0,0
        # self.lineaEjecutando = ""
        self.Vivo = True
        self.labels = {}
        self.PC = 0


    def __str__(self):
        tmp = f"Registros: {self.Registros} \n"
        # tmp += f"Linea Ejecutando: {self.lineaEjecutando} \n"
        tmp += f"Vivo: {self.Vivo} \n"
        tmp += f"Pos: {self.fila},{self.columna} \n"
        for l in self.Mapa:
            tmp += str(l) + "\n"
        return tmp

    def collect_labels(self, buffer):
        for pos,line  in enumerate(buffer):
            line = line.strip()
            if line.endswith(':'):
                label = line[:-1]  
                self.labels[label] = pos 


    def ejecutar_linea(self,linea):
        sentencia = linea.split(" ")

        match sentencia:
            case ["mov",Dir]: #2 arguments
                #implemetar actuador
                # if Dir in ["r","l","u","d"]:

                if Dir == "r":
                    self.columna += 1
                    if self.columna >= len(self.Mapa):
                        self.Vivo = False
                    if self.Vivo:
                        self.Mapa[self.fila][self.columna -1] = 0
                        self.Mapa[self.fila][self.columna] = 3

                elif Dir == "l":
                    self.columna -= 1
                    if self.columna < 0:
                        self.Vivo = False
                    if self.Vivo:
                        self.Mapa[self.fila][self.columna +1] = 0
                        self.Mapa[self.fila][self.columna] = 3
                        
                elif Dir == "u":
                    self.fila -= 1
                    if self.fila < 0:
                        self.Vivo = False
                    if self.Vivo:
                        self.Mapa[self.fila +1][self.columna] = 0
                        self.Mapa[self.fila][self.columna] = 3
                        
                elif Dir == "d":
                    self.fila += 1
                    if self.fila >= len(self.Mapa):
                        self.Vivo = False
                    if self.Vivo:
                        self.Mapa[self.fila -1][self.columna] = 0
                        self.Mapa[self.fila][self.columna] = 3

            case ["obs",Dir]: #2 arguments
                #implemetar sensor 
                # if Dir in ["r","l","u","d"]:
                self.Registros["DX"] = 0

                if Dir == "r":
                    if (self.columna)+1 == len(self.Mapa) \
                        or (self.Mapa[self.fila][self.columna +1] != 0): 
                        self.Registros["DX"] = 1
                    
                elif Dir == "l":
                    if (self.columna)-1 == -1 \
                        or (self.Mapa[self.fila][self.columna -1] != 0): 
                        self.Registros["DX"] = 1
                        
                elif Dir == "u":
                    if (self.fila)-1 == -1 \
                        or (self.Mapa[self.fila -1][self.columna] != 0): 
                        self.Registros["DX"] = 1

                        
                elif Dir == "d":
                    if (self.fila)+1 == len(self.Mapa) \
                        or (self.Mapa[self.fila +1][self.columna] != 0):
                        self.Registros["DX"] = 1


            case [Ins,Z1,Z2,Z3]: #4 arguments

                if Z1.startswith("0x"):
                    Z1 = int(Z1.split("x")[1])
                else:
                    Z1 = self.Registros[Z1]
                if Z2.startswith("0x"):
                    Z2 = int(Z2.split("x")[1])
                else:
                    Z2 = self.Registros[Z2]

                print(f"{Ins} {Z1} {Z2} {Z3}")

                if Ins[0] == "j":

                    if (Ins == "je" and Z1 == Z2) or (Ins == "jne" and Z1 != Z2):
                        self.PC = self.labels.get(Z3,self.PC) 
                    # else:
                        # self.PC += 1
                    
                    #jump
                else:
                    #Opmat

                    if Ins == "add":
                        self.Registros[Z3] = Z1 + Z2

                    if Ins == "sub":
                        self.Registros[Z3] = Z1 - Z2

                    if Ins == "mul":
                        self.Registros[Z3] = Z1 * Z2

                    if Ins == "div":
                        self.Registros[Z3] = int(Z1 / Z2)
