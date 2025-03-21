from ruamel.yaml import YAML

#Elimina conjunto de respuestas imposibles
def del_respuesta_imp(respuestas_pos,respuestas_act):
    n = len(respuestas_act)
    resultado = []
    [resultado.append(x) for x in respuestas_pos if respuestas_act == x[:n]]
    return resultado

#Verifica si es necesario hacer la siguiente pregunta
def verficar_preguntar(conjunto_res,res_act):
    n = len(res_act)
    for i in range(1,len(conjunto_res)):
        if conjunto_res[0][n] != conjunto_res[i][n]:
            return True
    return False

#Obtener animales
def obt_animales(res_act,animales,respuestas):
    animales_pos = [] 
    for i in range(len(animales)):
        if respuestas[i] == res_act:
            animales_pos.append(animales[i])
    return animales_pos

yaml = YAML()
yaml.default_flow_style = None 
yaml.indent(sequence=4, offset=2)

s = open("respuestas.yaml", "r")
Data = yaml.load(s)
s.close()

conjunto_res = []
[conjunto_res.append(x) for x in Data["respuestas"]["respuestas"] if x not in conjunto_res]

respuestas = Data["respuestas"]["respuestas"]
animales = Data["respuestas"]["animales"]
preguntas = Data["respuestas"]["caracteristicas"]

#Conjunto de respuestas con las que se trabajaran
respuestas_act = []

#¿Hay más de una respuesta posible? Se presupone que al inicio del programa si
ban1 = True 
#Contador de preguntas
cont_p = 0

while ban1:
    if verficar_preguntar(conjunto_res,respuestas_act):        
        respuestas_act.append(int(input(str(preguntas[cont_p])+" Si(1)/No(0): ")))
    else:
        respuestas_act.append(conjunto_res[0][len(respuestas_act)])
    cont_p += 1
    conjunto_res = del_respuesta_imp(conjunto_res,respuestas_act)
    if len(conjunto_res) <= 1:
            ban1 = False

if len(conjunto_res) == 0:
    print("Imposible adivinar")
else:
    animales_pos = obt_animales(conjunto_res[0],animales,respuestas)

    while len(animales_pos) > 1:
        x = input("Tu animal es "+str(animales_pos[0])+"? (S/n)")
        if x == "s" or x == "S":
            animales_pos = animales_pos[:1]
        else:
            animales_pos = animales_pos[1:]

    print("Estas pensando en",animales_pos[0])




