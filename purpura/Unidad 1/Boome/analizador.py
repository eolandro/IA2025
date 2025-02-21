def dlabel(label):
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
    R2 = Dir in ["r","l","u","d"]
    return R1 and R2

"""def opera_senact(SensorAct,Dir):
    return all([
        SensorAct in ["mov","obs"],
        Dir in ["r","l","u","d"]
    ])"""

def hexa(x):
    hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    if x[0] == "0" and x[1] == "x" and len(x) >= 3:
        for i in range(2,len(x)):
            if x[i] not in hex:
                return False
        return True
    return False

def registro(reg):
    return reg in ["AX","BX","CX","DX"]

def opera_salto(Salto,RegA,RegB,Lab):
    return all([
        Salto in ["je","jne"],
        registro(RegA) or hexa(RegA),
        registro(RegB) or hexa(RegB),
        Lab.isalpha() and Lab.isupper()
    ])

def opera_mat(Oper,RegA,RegB,RegC):
    return all([
        Oper in ["add","sub","mul","div"],
        registro(RegA) or hexa(RegA),
        registro(RegB) or hexa(RegB),
        registro(RegC)
    ])

def linea_codigo(linea):
    if not linea:
        return False
    lsep = linea.split(" ")
    match lsep:
        case [label]:
            return dlabel(label)
        case [SensorAct,Dir]:
            return opera_senact(SensorAct,Dir)
        case [Ins,Z1,Z2,Z3]:
            if Ins[0] == 'j': # Salto
                return opera_salto(Ins,Z1,Z2,Z3)
            else: # OpMat
                return opera_mat(Ins,Z1,Z2,Z3)
    return False