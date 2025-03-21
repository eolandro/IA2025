from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = False

def get_concurrencia(data_animalx,animales,data,columna,concurrencia,animales_aux=[],preguntas_aux=[]):
    if len(animales) == 0:
        return concurrencia,animales_aux
    data_animal0 = data[animales[0]][0][columna]
    if data_animal0 == data_animalx:
        animales_aux+=[animales[0]]
        return get_concurrencia(data_animalx,animales[1:],data,columna,concurrencia+1,animales_aux)
    else:
        return get_concurrencia(data_animalx,animales[1:],data,columna,concurrencia,animales_aux)


def Adivina_aux(preguntas,animales,data,columna):
    if len(preguntas) == 1:
        return animales[0],columna
    data_animal0 = data[animales[0]][0][columna]
    data_animal1 = data[animales[1]][0][columna]
    if data_animal0 != data_animal1:
        return preguntas[0],columna
    else:
        return Adivina_aux(preguntas[1:],animales,data,columna+1)


def Adivina(preguntas,animales,data,columna=0):
    if len(animales) == 1:
        return animales[0]
    data_animal0 = data[animales[0]][0][columna]
    data_animal1 = data[animales[1]][0][columna]
    if len(animales) == 2:
        x = input(f"is {preguntas[1]}?").strip().lower()
        if x == "y":
            return animales[0]
        elif x == "n":
            return animales[1]
        else:
            print("-- Respuesta inválida --")
            exit(1)
    # if data_animal0 == 0 and data_animal1 == 0:
    #     return Adivina(preguntas[1:],animales,data,columna+1)
    if data_animal0 == data_animal1:
        respX,columna_aux = Adivina_aux(preguntas[1:],animales,data,columna+1)
        # print(respX)
        # print(columna_aux)
        if respX:
            if respX in animales:
                x = input(f"is {respX}?").strip().lower()
                if x == "y":
                    return animales[0]
                elif x == "n":
                    return  Adivina(preguntas,animales[1:],data,columna) 
                else:
                    print("-- Respuesta inválida --")
                    exit(1)
            else:
                x = input(f"is {respX}?").strip().lower()
                if x == "y":
                    data_animalx = data[animales[0]][0][columna_aux]
                    concurrencia,animales_aux = get_concurrencia(data_animalx,animales,data,columna_aux,concurrencia=1)
                    # print(concurrencia)
                    # print(animales_aux)
                    # print(animales)
                    # print(all(i in animales for i in animales_aux)) 
                    if concurrencia == 1 :
                        return animales[0]
                    elif all(i in animales for i in animales_aux):
                        return Adivina(preguntas[1:],animales_aux,data,columna+1) 
                    else:
                        left_animals = list(filter(lambda x: x not in animales, animales_aux))
                        print(left_animals)
                        return Adivina(preguntas[1:],left_animals,data,columna+1) 

                elif x == "n":
                    data_animalx = data[animales[0]][0][columna_aux]
                    concurrencia,animales_aux = get_concurrencia(data_animalx,animales,data,columna_aux,concurrencia=1)
                    # print(concurrencia)
                    # print(animales_aux)
                    # print(animales)
                    # print(preguntas[1:])
                    # print(all(i in animales for i in animales_aux)) 
                    if concurrencia == 1 :
                        left_animals = list(filter(lambda x: x not in animales_aux, animales))
                        # print(left_animals)
                        return Adivina(preguntas[1:],animales[1:],data,columna) 
                    else:
                        left_animals = list(filter(lambda x: x not in animales_aux, animales))
                        # print(left_animals)
                        return Adivina(preguntas[1:],left_animals,data,columna+1) 
                else:
                    print("-- Respuesta inválida --")
                    exit(1)
    else:
        x = input(f"is {preguntas[0]}?").strip().lower()
        if x == "y":
            return animales[0]
        elif x == "n":
            # print(preguntas[1:])
            # print(animales[1:])
            return  Adivina(preguntas[1:],animales[1:],data,columna+1) 
        else:
            print("-- Respuesta inválida --")
            exit(1)
    
with open("tabla.yaml", "r") as tabla, open("preguntasAnimales.yaml", "r") as data:

    datos = yaml.load(data)
    preguntas = datos['preguntas']
    preguntas.reverse()
    print(list(preguntas))

    table_data = yaml.load(tabla)
    animales = list(table_data.keys())
    print(animales)

    Animal = Adivina(preguntas,animales,table_data)
    print(f"El animal es: {Animal}")     
