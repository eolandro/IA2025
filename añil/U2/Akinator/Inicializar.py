from ruamel.yaml import YAML

yaml = YAML()
yaml.default_flow_style = False


with open("preguntasAnimales.yaml", "w") as init_data:
    # nAnimales = str(input("Igresa la Cantidad de Animales: >"))
    nAnimales = 10
    nPreguntas = nAnimales 

    animals = []
    for i in range (nAnimales):
        animals += [input(f"ingresa al {i+1}° Animal: >")]
    yaml.dump({'animales': animals}, init_data)

    questions = []
    for i in range (nPreguntas):
        questions += [input(f"ingresa la #{i+1}° pregunta: >")]
    yaml.dump({'preguntas': questions}, init_data)

    print("---- saved in \"preguntas.yaml\" ----")


