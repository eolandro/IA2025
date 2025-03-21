from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = True 

with open('preguntasAnimales.yaml', 'r') as file:

    data = yaml.load(file)
    # data = yaml.load(file)
    #datos de preguntas y animales
    print(data)
    valores_tabla = {}

    animales = data['animales']

    for animal in animales:
        val = []
        potencia = 0
        for pregunta in data['preguntas']:
            x = input(f"{animal} -> {pregunta} (Y/n): >").strip().lower()
            if x == "y":
                print(True)
                val += [pow(2,potencia)]
            elif x == "n":
                print(False)
                val += [0]
            else:
                print("-- Respuesta inválida --")
                exit(1)
            potencia += 1

        val = val[::-1]
        valores_tabla[animal] = [val,[sum(val)]]

        print(valores_tabla)


    #sorting based on the last value
    valores_tabla_sorted = dict(sorted(valores_tabla.items(), key=lambda x: x[1][1], reverse=True))


#savinn
with open('tabla.yaml', 'w') as tabla:
    yaml.dump(valores_tabla_sorted, tabla)


    
    
