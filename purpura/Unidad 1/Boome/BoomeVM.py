class BoomeVM:
    def __init__(self): #constructor
        self.Registros = {
            "AX": hex(0),
            "BX": hex(0),
            "CX": hex(0),
            "DX": hex(0),
        }
        #0: nada
        #1: obstáculo
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
        self.salto = None

    def __str__(self):
        tmp = f"Registros: {self.Registros} \n"
        tmp += f"Linea Ejecutando: {self.lineaEjecutando} \n"
        tmp += f"Vivo: {self.Vivo} \n"
        tmp += f"Pos: {self.fila},{self.columna} \n"
        for l in self.Mapa:
            tmp += str(l) + "\n"
        return tmp
    
    def ejectuar_linea(self,linea):
        self.salto = None
        sentencia = linea.split(" ")
        match sentencia:
            case[label]:
                pass
            case["mov","r"]:
                if self.columna+1 >= len(self.Mapa[self.fila]):
                    self.Vivo = False
                elif self.Mapa[self.fila][self.columna+1] >= 1:
                    self.Vivo = False
                self.columna = self.columna + 1
                if self.Vivo:
                    self.Mapa[self.fila][self.columna-1] = 0
                    self.Mapa[self.fila][self.columna] = 3
            case["mov","l"]:
                if self.columna <= 0:
                    self.Vivo = False
                elif self.Mapa[self.fila][self.columna-1] >= 1:
                    self.Vivo = False
                self.columna = self.columna - 1
                if self.Vivo:
                    self.Mapa[self.fila][self.columna+1] = 0
                    self.Mapa[self.fila][self.columna] = 3
            case["mov","d"]:
                if self.fila >= len(self.Mapa[self.columna]):
                    self.Vivo = False
                elif self.Mapa[self.fila+1][self.columna] >= 1:
                    self.Vivo = False
                self.fila = self.fila + 1
                if self.Vivo:
                    self.Mapa[self.fila - 1][self.columna] = 0
                    self.Mapa[self.fila][self.columna] = 3
            case["mov","u"]:
                if self.fila <= 0:
                    self.Vivo = False
                elif self.Mapa[self.fila-1][self.columna] >= 1:
                    self.Vivo = False
                self.fila = self.fila - 1
                if self.Vivo:
                    self.Mapa[self.fila + 1][self.columna] = 0
                    self.Mapa[self.fila][self.columna] = 3
            case["obs","r"]:
                if self.columna + 1 >= len(self.Mapa[self.fila]):
                    self.Registros["DX"] = hex(1)
                elif self.Mapa[self.fila][self.columna + 1] >= 1:
                    self.Registros["DX"] = hex(1)
                else:
                    self.Registros["DX"] = hex(0)
            case["obs","l"]:
                if self.columna - 1 < 0:
                    self.Registros["DX"] = hex(1)
                elif self.Mapa[self.fila][self.columna - 1] >= 1:
                    self.Registros["DX"] = hex(1)
                else:
                    self.Registros["DX"] = hex(0)
            case["obs","d"]:
                if self.fila + 1 >= len(self.Mapa[self.columna]):
                    self.Registros["DX"] = hex(1)
                elif self.Mapa[self.fila + 1][self.columna] >= 1:
                    self.Registros["DX"] = hex(1)
                else:
                    self.Registros["DX"] = hex(0)
            case["obs","u"]:
                if self.fila - 1 < 0:
                    self.Registros["DX"] = hex(1)
                elif self.Mapa[self.fila - 1][self.columna] >= 1:
                    self.Registros["DX"] = hex(1)
                else:
                    self.Registros["DX"] = hex(0)
            case [Ins,Z1,Z2,Z3]:
                if Z1 in self.Registros.keys():
                    Z1 = self.Registros[Z1]
                if Z2 in self.Registros.keys():
                    Z2 = self.Registros[Z2]
                if Ins[0] == 'j': 
                    if Ins == "je":
                        if int(Z1,16) == int(Z2,16):
                            self.salto = Z3
                    if Ins == "jne":
                        if int(Z1,16) != int(Z2,16):
                            self.salto = Z3
                else:
                    match Ins:
                        case "add":
                            self.Registros[Z3] = hex(int(Z1,16) + int(Z2,16))
                        case "sub":
                            self.Registros[Z3] = hex(int(Z1,16) - int(Z2,16))
                        case "mul":
                            self.Registros[Z3] = hex(int(Z1,16) * int(Z2,16))
                        case "div":
                            self.Registros[Z3] = hex(int(Z1,16) // int(Z2,16))
                            
                            
