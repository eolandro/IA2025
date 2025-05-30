import re

def esEtiquetaValida(etiqueta):
    if not etiqueta.endswith(":"):
        return False
    nombre = etiqueta[:-1]
    return nombre.isdigit() or (nombre.isalnum() and nombre.isupper())

def esInstruccionSensor(accion, direccion):
    acciones_validas = {"mov", "obs"}
    direcciones_validas = {"l", "u", "r", "d"}
    return accion in acciones_validas and direccion in direcciones_validas

def esHexORegistro(valor, permitir_hex=True):
    if valor in {"AX", "BX", "CX", "DX"}:
        return True
    if permitir_hex:
        try:
            int(valor, 16)
            return valor.startswith("0x") and len(valor) == 4
        except ValueError:
            return False
    return False

def esInstruccionSalto(instruccion, op1, op2, destino):
    if destino in {"AX", "BX", "CX", "DX"}:
        return False
    if not destino.endswith(":"):
        destino += ":"
    return (instruccion in {"je", "jne"} and
            esHexORegistro(op1) and
            esHexORegistro(op2) and
            esEtiquetaValida(destino))

def esInstruccionMatematica(instruccion, op1, op2, op3):
    return (instruccion in {"add", "sub", "mul", "div"} and
            esHexORegistro(op1) and
            esHexORegistro(op2) and
            esHexORegistro(op3, permitir_hex=False))

def validarLinea(linea):
    if not linea.strip():
        return False
    partes = linea.split()
    
    if len(partes) == 1:
        return esEtiquetaValida(partes[0])
    
    if len(partes) == 2:
        return esInstruccionSensor(partes[0], partes[1])
    
    if len(partes) == 4:
        if partes[0].startswith("j"):
            return esInstruccionSalto(partes[0], partes[1], partes[2], partes[3])
        else:
            return esInstruccionMatematica(partes[0], partes[1], partes[2], partes[3])
    
    return False