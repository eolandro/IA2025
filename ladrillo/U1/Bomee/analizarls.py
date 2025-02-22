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
        return re.fullmatch(r"^0x[0-9a-fA-F]{2}$", valor) is not None
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
    if not linea:
        return False
    partes = linea.split()
    match partes:
        case [etiqueta]:
            return esEtiquetaValida(etiqueta)
        case [accion, direccion]:
            return esInstruccionSensor(accion, direccion)
        case [instruccion, op1, op2, op3]:
            if instruccion.startswith("j"):
                return esInstruccionSalto(instruccion, op1, op2, op3)
            else:
                return esInstruccionMatematica(instruccion, op1, op2, op3)
    return False