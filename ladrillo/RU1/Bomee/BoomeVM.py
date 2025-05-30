from analizarls import esEtiquetaValida

class BoomeVM:
    def __init__(self):
        self.registrosCPU = {"AX": 0x00, "BX": 0x00, "CX": 0x00, "DX": 0x00}
        self.mapa = [
            ["B", 0, 0, 0, 0, 0, 0, 0],  # "B" posición inicial boome
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.fila, self.columna = 0, 0
        self.instruccionActual = ""
        self.estaVivo = True
        self.etiquetas = {}

    def __str__(self):
        estado = f"Registros: {self.registrosCPU}\n"
        estado += f"Instrucción: {self.instruccionActual}\n"
        estado += f"Vivo: {self.estaVivo}\n"
        estado += f"Posición: {self.fila}, {self.columna}\n\n"
        for fila in self.mapa:
            estado += str(fila) + "\n"
        return estado

    def obtenerValor(self, valor):
        if valor in self.registrosCPU:
            return self.registrosCPU[valor]
        elif valor.startswith("0x"):
            return int(valor, 16)
        else:
            return int(valor)

    def procesarInstruccion(self, linea, lineasCodigo, indice):
        self.instruccionActual = linea.strip()
        partes = linea.split()
        
        match partes:
            case [etiqueta]:
                if esEtiquetaValida(etiqueta):
                    self.etiquetas[etiqueta[:-1]] = indice
                return indice + 1

            case ["mov", direccion]:
                # Limpiar posición anterior
                if 0 <= self.fila < len(self.mapa) and 0 <= self.columna < len(self.mapa[0]):
                    self.mapa[self.fila][self.columna] = 0
                
                # Mover
                if direccion == "r":
                    self.columna += 1
                elif direccion == "l":
                    self.columna -= 1
                elif direccion == "u":
                    self.fila -= 1
                elif direccion == "d":
                    self.fila += 1
                
                # Verifica posición
                if not (0 <= self.fila < len(self.mapa)) or not (0 <= self.columna < len(self.mapa[0])):
                    self.estaVivo = False
                elif self.mapa[self.fila][self.columna] == 2:
                    self.estaVivo = False
                    self.mapa[self.fila][self.columna] = "B" 
                else:
                    self.mapa[self.fila][self.columna] = "B"  
                return indice + 1

            case ["obs", direccion]:
                if direccion == "r":
                    self.registrosCPU["DX"] = 0x01 if (
                        self.columna + 1 >= len(self.mapa[0]) or
                        self.mapa[self.fila][self.columna + 1] in {1, 2}
                    ) else 0x00
                elif direccion == "l":
                    self.registrosCPU["DX"] = 0x01 if (
                        self.columna - 1 < 0 or
                        self.mapa[self.fila][self.columna - 1] in {1, 2}
                    ) else 0x00
                elif direccion == "u":
                    self.registrosCPU["DX"] = 0x01 if (
                        self.fila - 1 < 0 or
                        self.mapa[self.fila - 1][self.columna] in {1, 2}
                    ) else 0x00
                elif direccion == "d":
                    self.registrosCPU["DX"] = 0x01 if (
                        self.fila + 1 >= len(self.mapa) or
                        self.mapa[self.fila + 1][self.columna] in {1, 2}
                    ) else 0x00
                return indice + 1

            case [instruccion, op1, op2, op3]:
                if instruccion.startswith("j"):
                    if op3.rstrip(":") in self.etiquetas:
                        if instruccion == "je" and self.obtenerValor(op1) == self.obtenerValor(op2):
                            return self.etiquetas[op3.rstrip(":")]
                        elif instruccion == "jne" and self.obtenerValor(op1) != self.obtenerValor(op2):
                            return self.etiquetas[op3.rstrip(":")]
                else:
                    
                    valor1 = self.obtenerValor(op1)
                    valor2 = self.obtenerValor(op2)
                    registro_destino = op3
                    
                    if instruccion == "add":
                        self.registrosCPU[registro_destino] = (valor1 + valor2) & 0xFF
                    elif instruccion == "sub":
                        self.registrosCPU[registro_destino] = (valor1 - valor2) & 0xFF
                    elif instruccion == "mul":
                        self.registrosCPU[registro_destino] = (valor1 * valor2) & 0xFF
                    elif instruccion == "div":
                        if valor2 == 0:
                            self.estaVivo = False
                        else:
                            self.registrosCPU[registro_destino] = (valor1 // valor2) & 0xFF
                return indice + 1