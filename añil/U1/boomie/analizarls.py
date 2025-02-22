#!/usr/bin/env python3

import re

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
    return all([
        SensorAct in ["mov","obs"],
        Dir in ["r","l","u","d"]
    ])

#creating the hex pattern using a raw string
hex_pattern = r"0x([0-9a-f][0-9a-f])"
# label_pattern = r"([0-9A-Fa-f]*:"

def opera_salto(jump,z1,z2,label):
    return all([
        jump in ["je","jne"],
        z1 in ["AX","BX","CX","DX"] or re.match(hex_pattern,z1), 
        z2 in ["AX","BX","CX","DX"] or re.match(hex_pattern,z2), 
        dlabel(f"{label}:")
    ])


def opera_mat(Op,Z1,Z2,Z3):
    return all([
        Op in ["add","sub","mul","div"],
        Z1 in ["AX","BX","CX","DX"] or re.match(hex_pattern,Z1),
        Z2 in ["AX","BX","CX","DX"] or re.match(hex_pattern,Z2),
        Z3 in ["AX","BX","CX","DX"] 
    ])

def linea_codigo(linea):
    if not linea:
        return False
    lsep = linea.split(" ")
    match lsep:
        case [label]: #1 argument 
            return dlabel(label)
        case [SensorAct,Dir]: #2 arguments
            return opera_senact(SensorAct,Dir)
        case [Ins,Z1,Z2,Z3]: #4 arguments
            if Ins[0] == "j":
                #jump
                return opera_salto(Ins,Z1,Z2,Z3)
            else:
                #Opmat
                return opera_mat(Ins,Z1,Z2,Z3)
    return False





