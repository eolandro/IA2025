import random, numpy, secrets
from ruamel.yaml import YAML
from faker import Faker
yaml=YAML()
yaml.default_flow_style =False
yaml.indent(sequence=4, offset=2)

s=open("tablero.yaml","r")
Data = yaml.load(s)
s.close()

def generador():
    elec = int(input("Elige un generador: \n- Random(default)(0)\n- numpy(1)\n- faker(2)\n- secrets(3)\n-----> "))
    match elec:
        case 0:
            return random.choice
        case 1:
            return numpy.random.choice
        case 3:
            return secrets.choice
        case 2:
            f = Faker()
            return f.random_element

lista_bomba = [1,1,1,1,1,1,1,1,1,0]
lista_vacio = [0,0,0,0,0,0,0,0,1,1]

tabla = []
cont_celdas = 0
cont_bombas = 1

for i in Data["tablero"]:
    tabla.append(i)
    cont_celdas+=len(i)

x = 0
y = 0

cont_celdas_pas = 0

p_bomba = 1/cont_celdas
p_no_bomba = 1-p_bomba

p_bomba_det = {1:0.9,0:0.1}
p_no_bomba_det = {1:0.2,0:0.8}

p_total_pos = p_bomba*p_bomba_det[1]+p_no_bomba*p_no_bomba_det[1]
p_total_neg = p_bomba*p_bomba_det[0]+p_no_bomba*p_no_bomba_det[0]

p_bay = 0


def encuentra_bomba(tabla,p_bomba,cont_celdas,cont_celdas_pas,p_bomba_det,p_no_bomba,p_no_bomba_det,generar):
    for x in range(len(tabla)):
        for y in range(len(tabla[x])):
            for i in range(3):
                if tabla[x][y]:
                    det = generar(lista_bomba)
                else:
                    det = generar(lista_vacio)
                if det:
                    p_bomba = p_bomba_det[det]*p_bomba/(p_bomba*p_bomba_det[det]+p_no_bomba*p_no_bomba_det[det])
                    p_no_bomba = 1-p_bomba
                    print("La probabilidad de Bayes en casilla "+str(x)+","+str(y)+" es de "+str(p_bomba))
                if p_bomba > 0.5:
                    print("Bomba encontrada")
                    return (x,y)
            cont_celdas_pas+=1
            p_bomba=1/(cont_celdas-cont_celdas_pas)
            p_no_bomba=1-p_bomba
    return


bomba_adiv = encuentra_bomba(tabla,p_bomba,cont_celdas,cont_celdas_pas,p_bomba_det,p_no_bomba,p_no_bomba_det,generador())
if not bomba_adiv:
    print("Bomee no encontró la bomba")
else:
    if tabla[bomba_adiv[0]][bomba_adiv[1]]:
        print("Bomee encontró la bomba exitosamente")
    else:
        print("Bomee voló por los aires :d")
            