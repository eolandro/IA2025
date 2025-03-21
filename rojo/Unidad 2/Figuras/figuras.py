from ruamel.yaml import YAML

def cargar_datos():
    yaml = YAML()
    with open("figuras.yaml", "r", encoding="utf-8") as file:
        return yaml.load(file)

def obtener_pregunta(id_pregunta, data):
    return next((pregunta[1] for pregunta in data['preguntas'] if pregunta[0] == id_pregunta), None)

def opciones_disponibles(nodo_actual, data):
    return [opcion[1] for opcion in data['arbolopcion'] if opcion[0] == nodo_actual]

def siguiente_nodo(nodo_actual, respuesta, data):
    return next((opcion[2] for opcion in data['arbolopcion'] if opcion[0] == nodo_actual and opcion[1] == respuesta), None)

def mostrar_figuras(data):
    print("\n"+"Figuras que puedes escoger:")
    figuras_terminales = list(filter(lambda x: ')' not in x[1], data['preguntas']))
    for figura in figuras_terminales:
        print("--> " + figura[1])

def adivinador():
    data = cargar_datos()
    mostrar_figuras(data)
    nodo_actual = 'A'
    
    while True:
        print("\n")
        pregunta = obtener_pregunta(nodo_actual, data)
        opciones = opciones_disponibles(nodo_actual, data)
        
        if pregunta and pregunta.endswith(')'):
            while True:
                if nodo_actual == 'A':
                    respuesta = input(f"{pregunta} Opciones {opciones}: ").strip().capitalize()
                else:
                    respuesta = input(f"{pregunta}: ").strip().capitalize()
                
                nodo_siguiente = siguiente_nodo(nodo_actual, respuesta, data)
                
                if nodo_siguiente:
                    nodo_actual = nodo_siguiente
                    break
                else:
                    print("Respuesta no permitida. Intenta de nuevo.")
        else:
            print(f"\n¡Tu figura es un {pregunta}!")
            break

if __name__ == "__main__":
    adivinador()
