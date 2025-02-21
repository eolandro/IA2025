import re

def dLabel(label):
    if label[-1] != ":":
        return False
    lb = label[:-1]
    if lb.isdigit():
        return True
    elif lb.isalnum() and lb.isupper():
        return True
    return False

def opera_senact(SensorAct,Dir):
    R1 = SensorAct in ["mov","obs"]
    R2 = Dir in ["l","u","r","d"]
    return R1 and R2

def HexReg(Z, Fl=True):
    Hexa = r"^0x[0-9a-fA-F]{2}$"
    if Z in ["AX", "BX", "CX", "DX"]:
        return True
    return Fl and re.fullmatch(Hexa, Z)

def opera_salto(Ins,Z1,Z2,Z3):
    if Z3 in ["AX", "BX", "CX", "DX"]:
        return False
    if Z3[-1] != ":":
        Z3 += ":"
    return all([Ins in ["je","jne"],
    HexReg(Z1),
    HexReg(Z2),
    dLabel(Z3)
    ])
    
def opera_mat(Ins,Z1,Z2,Z3):
    return all([Ins in ["add", "sub", "mul", "div"],
    HexReg(Z1),
    HexReg(Z2),
    HexReg(Z3, Fl=False)
    ])

# * ------------------------ MAIN ------------------------ # *
# TODO: import analizadorLS
# TODO: analizadorLS.linea_codigo("")
def linea_codigo(linea):
    if not linea:
        return False
    lsep = linea.split(" ")
    match lsep:
        case [label]: # ! 1
            return dLabel(label)
        case [SensorAct,Dir]: # ! 2
            return opera_senact(SensorAct,Dir)
        case [Ins,Z1,Z2,Z3]: # ! 4
            if(Ins[0] == "j"): # ! Salto
                return opera_salto(Ins,Z1,Z2,Z3)
            else:
                return opera_mat(Ins,Z1,Z2,Z3) # ! operación
    return False