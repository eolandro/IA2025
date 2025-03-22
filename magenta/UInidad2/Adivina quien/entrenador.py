from ruamel.yaml import YAML

def cargar_preguntas():
    yaml = YAML()
    with open("preguntas_animales.yaml", "r") as archivo:
        return yaml.load(archivo)

def hacer_preguntas(datos):
    animales = datos["animales"]
    caracteristicas = datos["caracteristicas"]
    tabla = {animal: {caracteristica: None for caracteristica in caracteristicas} for animal in animales}
    
    for animal in animales:
        print("\nEvaluando el animal: " + animal + "\n")
        for caracteristica in caracteristicas:
            respuesta = input("¿El animal " + animal + " tiene la característica '" + caracteristica + "'? (S/N): ").strip()
            if respuesta.lower() == 's':
                tabla[animal][caracteristica] = 1
            elif respuesta.lower() == 'n':
                tabla[animal][caracteristica] = 0

    return tabla

def guardar_tabla(tabla):
    yaml = YAML()
    with open("tabla.yaml", "w") as archivo:
        yaml.dump(tabla, archivo)
    print("Tabla guardada en tabla.yaml")

def puntuar_tabla(tabla):
    puntajes = {}
    for animal, caracteristicas in tabla.items():
        # Asegurarnos de que solo sumamos los valores válidos (0 o 1)
        puntaje = sum(1 for v in caracteristicas.values() if v == 1)
        puntajes[animal] = puntaje
    
    # Ordenar los animales por puntaje (de mayor a menor)
    puntajes_ordenados = {k: v for k, v in sorted(puntajes.items(), key=lambda item: item[1], reverse=True)}
    return puntajes_ordenados

def main():
    datos = cargar_preguntas()

    tabla = hacer_preguntas(datos)
    
    guardar_tabla(tabla)

    puntajes_ordenados = puntuar_tabla(tabla)
   
    print("\nPuntajes de los animales (ordenados):")
    for animal, puntaje in puntajes_ordenados.items():
        print(animal + ": " + str(puntaje) + " puntos")

if __name__ == "__main__":
    main()
